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

class PostDetail(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def update(self, request, *args, **kwargs):
        user = request.user
        liked_by = self.get_object().liked_by
        if user in list(liked_by.all()):
            liked_by.remove(user)
        else:
            liked_by.add(user)
        serializer = self.get_serializer(self.get_object(), {'liked_by': liked_by}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
