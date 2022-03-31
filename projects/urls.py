

from django.urls import path
from .views import ProjectViewset
from rest_framework.routers import DefaultRouter

router = router = DefaultRouter()
router.register('', ProjectViewset, basename="projects")
urlpatterns = router.urls