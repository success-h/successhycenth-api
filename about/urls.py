from django.urls import path
from .views import AboutViewset
from rest_framework.routers import DefaultRouter

router = router = DefaultRouter()
router.register('', AboutViewset, basename="about")
urlpatterns = router.urls