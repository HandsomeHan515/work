from django.conf.urls import url
from rest_framework import routers

from .views import (
    LoginView, LogoutView, UserDetailView, PasswordChangeView, Register,
    PasswordResetView, PasswordResetConfirmView, verify_code
)

router = routers.SimpleRouter()

urlpatterns = [
    # URLs that do not require a session or valid token
    url(r'^password/reset/$', PasswordResetView.as_view(),
        name='rest_password_reset'),
    url(r'^password/reset/confirm/$', PasswordResetConfirmView.as_view(),
        name='rest_password_reset_confirm'),
    url(r'^password/change/$', PasswordChangeView.as_view(),
        name='rest_password_change'),

    url(r'^verify/$', verify_code, name='verify_code'),
    url(r'^login/$', LoginView.as_view(), name='rest_login'),
    url(r'^register/$', Register.as_view(), name='register'),
    # URLs that require a user to be logged in with a valid session / token.
    url(r'^logout/$', LogoutView.as_view(), name='rest_logout'),
    url(r'^detail/$', UserDetailView.as_view(), name='rest_user_details'),
]

urlpatterns += router.urls
