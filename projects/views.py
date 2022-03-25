from rest_framework.generics import ListAPIView
from rest_framework import permissions

from .models import Works
from .serializers import ProjectSerializer


class ProjectListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Works.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = None