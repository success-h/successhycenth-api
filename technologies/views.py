from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TechnologySerializer
from .models import Technology

# Create your views here.

class TechnologyViewset(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer