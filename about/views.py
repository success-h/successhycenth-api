from rest_framework.generics import ListAPIView
from rest_framework import viewsets

from .models import About
from .serializers import AboutSerializer


class AboutViewset(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
