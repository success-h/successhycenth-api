from django.urls import path
from .views import TechnologyViewset
from rest_framework.routers import DefaultRouter

router = router = DefaultRouter(trailing_slash=False)
router.register('', TechnologyViewset)
urlpatterns = router.urls