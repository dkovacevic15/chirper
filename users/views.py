from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from users.serializers import UserSerializer, UserListSerializer
from users.permissions import IsUserOrReadOnly, GetOrPostOnly
# Create your views here.
class UserList(generics.ListCreateAPIView):
    permission_classes = (GetOrPostOnly,)
    queryset = User.objects.all()
    serializer_class = UserListSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsUserOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
