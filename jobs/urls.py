from django.conf.urls import url
from rest_framework import routers
from .views import JobViewSet, JobLevelOneViewSet, JobLevelOneViewSet

urlpatterns = []

router = routers.SimpleRouter()
router.register('^levelone', JobLevelOneViewSet)
router.register('^leveltwo', JobLevelOneViewSet)
router.register('', JobViewSet)

urlpatterns += router.urls
