from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TechnolofySerializer
from .models import Technology

# Create your views here.

class TechnologyViewset(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnolofySerializer