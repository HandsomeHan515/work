from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from .models import Ablity, AblityLevelOne, AblityLevelTwo
from .serializers import AblitySerializer, AblityLevelOneSerializer, AblityLevelTwoSerializer, AblityListSerializer


def PageResponse(self, data, serializer_class):
    page = self.paginate_queryset(data)
    if page is not None:
        serialize = serializer_class(
            page,
            many=True,
            context={'request': self.request},
        )
        return self.get_paginated_response(serialize.data)

    serializer = serializer_class(
        data,
        many=True,
        context={'request': self.request},
    )
    return Response(serializer.data)


class AblityViewSet(viewsets.ModelViewSet):
    queryset = Ablity.objects.all()
    serializer_class = AblitySerializer

    def list(self, *args, **kwargs):
        queryset = self.get_queryset()
        return PageResponse(self, queryset, AblityListSerializer)

    @list_route(methods=['POST'])
    def search(self, request):
        keyword = request.data['keyword']
        queryset = self.get_queryset().filter(Q(name__contains=keyword) |
                                              Q(level_two__name__contains=keyword))
        return PageResponse(self, queryset, AblityListSerializer)


class AblityLevelOneViewSet(viewsets.ModelViewSet):
    queryset = AblityLevelOne.objects.all()
    serializer_class = AblityLevelOneSerializer


class AblityLevelTwoViewSet(viewsets.ModelViewSet):
    queryset = AblityLevelTwo.objects.all()
    serializer_class = AblityLevelTwoSerializer
