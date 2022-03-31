from django.urls import path
from .views import TechnologyViewset
from rest_framework.routers import DefaultRouter

router = router = DefaultRouter()
router.register('', TechnologyViewset, basename="technologies")
urlpatterns = router.urls