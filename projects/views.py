from rest_framework import viewsets
from .models import Works
from .serializers import ProjectSerializer


class ProjectViewset(viewsets.ModelViewSet):
    queryset = Works.objects.all()
    serializer_class = ProjectSerializer
