from rest_framework import serializers
from users.serializers import UsernameOnlySerializer
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    liked_by = UsernameOnlySerializer(read_only=True, many=True)
    author = UsernameOnlySerializer(read_only=True, many=False)
    class Meta:
        model = Post
        fields = ('author', 'content', 'posted', 'liked_by')