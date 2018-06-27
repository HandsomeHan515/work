from django.conf.urls import url
from rest_framework import routers
from .views import AblityViewSet, AblityLevelOneViewSet, AblityLevelTwoViewSet

urlpatterns = []

router = routers.SimpleRouter()
router.register('^levelone', AblityLevelOneViewSet)
router.register('^leveltwo', AblityLevelTwoViewSet)
router.register('', AblityViewSet)

urlpatterns += router.urls
