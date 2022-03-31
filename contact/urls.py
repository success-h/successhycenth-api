from django.urls import path
from .views import ContactViewset
from rest_framework.routers import DefaultRouter

router = router = DefaultRouter()
router.register('', ContactViewset, basename="contact")
urlpatterns = router.urls