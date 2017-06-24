from rest_framework import serializers

from posts.models import Post
from django.contrib.auth.models import User

# The serializers could've probably been made more generic by asking for a fields paramater from the caller,
# but I feel this would be tempting fate on my part

class UsernameOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class UserSerializer(serializers.ModelSerializer):
    # posts = PostTextOnlySerializer(read_only=True, many=True) ????
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all().order_by('-posted'))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'posts')