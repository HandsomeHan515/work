from django.shortcuts import render

from django.contrib.auth import (
    login as django_login, logout as django_logout)
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.debug import sensitive_post_parameters

from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view

import random

from .serializers import (
    LoginSerializer, UserDetailSerializer, PasswordChangeSerializer,
    PasswordResetConfirmSerializer, PasswordResetSerializer, UserRegisterSrializer,
    JWTSerializer,
)

UserModel = get_user_model()

from utils.jwt import jwt_encode
from utils.check import is_mobile_num

# Create your views here.

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters(
        'password', 'old_password', 'new_password1', 'new_password2'
    )
)


@api_view(['POST'])
def verify_code(request):
    mobile = request.data['mobile']
    if not is_mobile_num(mobile):
        return Response({'text': 'invalid phone number'}, status=status.HTTP_400_BAD_REQUEST)

    code = random.randint(1000, 9999)

    return Response({'code': code}, status=status.HTTP_200_OK)


class Register(GenericAPIView):
    '''
    User register
    '''
    serializer_class = UserRegisterSrializer

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data)
        self.serializer.is_valid(raise_exception=True)

        username = self.serializer.validated_data['username']
        password = self.serializer.validated_data['password']
        nickname = self.serializer.validated_data['nickname']
        user = UserModel.objects.create(username=username, nickname=nickname)
        user.set_password(password)
        user.save()

        # generate seria code

        # serializer_class = UserDetailSerializer
        # serializer = serializer_class(instance={"users":user}, context={
        #                         'request': self.request})

        return Response({"id": user.id, "username": username}, status=status.HTTP_200_OK)


class LoginView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)

    def process_login(self):
        django_login(self.request, self.user)

    def login(self):
        self.user = self.serializer.validated_data['user']

        self.token = jwt_encode(self.user)

        self.process_login()

    def get_response(self):
        serializer_class = JWTSerializer

        data = {
            'user': self.user,
            'token': self.token
        }

        serializer = serializer_class(instance=data, context={
                                      'request': self.request})

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data)
        self.serializer.is_valid(raise_exception=True)

        self.login()
        return self.get_response()


class LogoutView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        return self.logout(request)

    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        django_logout(request)

        return Response({"detail": _("Successfully logged out.")}, status=status.HTTP_200_OK)


class UserDetailView(RetrieveUpdateAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return get_user_model().objects.none()


class PasswordResetView(GenericAPIView):
    """
    FixMe: This is not safey method for customer
    """
    serializer_class = PasswordResetSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        # Create a serializer with request.data
        self.serializer = self.get_serializer(data=request.data)
        self.serializer.is_valid(raise_exception=True)

        password = self.serializer.validated_data['password']
        username = self.serializer.validated_data['username']

        user = UserModel.objects.get(username=username)
        user.set_password(password)
        user.save()

        return Response({"id": user.id, "username": username}, status=status.HTTP_200_OK)


class PasswordResetConfirmView(GenericAPIView):
    """
    Password reset e-mail link is confirmed, therefore
    this resets the user's password.

    Accepts the following POST parameters: token, uid,
        new_password1, new_password2
    Returns the success/fail message.
    """
    serializer_class = PasswordResetConfirmSerializer
    permission_classes = (AllowAny,)

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(PasswordResetConfirmView, self).dispatch(*args, **kwargs)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"detail": _("Password has been reset with the new password.")}
        )


class PasswordChangeView(GenericAPIView):
    """
    Calls Django Auth SetPasswordForm save method.

    Accepts the following POST parameters: new_password1, new_password2
    Returns the success/fail message.
    """
    serializer_class = PasswordChangeSerializer
    permission_classes = (IsAuthenticated,)

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(PasswordChangeView, self).dispatch(*args, **kwargs)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": _("New password has been saved.")})
