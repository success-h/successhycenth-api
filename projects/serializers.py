from rest_framework import serializers
from .models import Tag, Works


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class ProjectSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Works
        fields = ('name', 'description', 'link', 'image', 'tags')