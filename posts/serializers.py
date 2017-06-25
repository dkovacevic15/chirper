from rest_framework import serializers

from posts.models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    liked_by = serializers.SlugRelatedField(many=True, read_only=True, slug_field='username')
    class Meta:
        model = Post
        fields = ('author', 'content', 'posted', 'liked_by')
