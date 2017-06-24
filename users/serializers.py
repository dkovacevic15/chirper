from rest_framework import serializers

from posts.models import Post
from django.contrib.auth.models import User

class UsernameOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'firstname', 'lastname', 'email')