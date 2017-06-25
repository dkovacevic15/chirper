from django.shortcuts import render
from posts.models import Post
from rest_framework import generics, permissions
from rest_framework.response import Response
from posts.serializers import PostSerializer
from posts.permissions import IsOwnerOrReadOnly

class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer