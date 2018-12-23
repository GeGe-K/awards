from rest_framework import serializers
from .models import Profile, Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'profile_pic', 'bio','contacts')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'description', 'image', 'url', 'user', 'pub_date')
