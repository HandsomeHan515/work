from django.conf.urls import url
from rest_framework import routers
from .views import QuestionViewSet

urlpatterns = []

router = routers.SimpleRouter()
router.register('', QuestionViewSet)

urlpatterns += router.urls
