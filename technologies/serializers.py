from rest_framework import serializers
from .models import Technology

class TechnolofySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = "__all__"