from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from users.serializers import UserSerializer
from users.permissions import IsUserOrReadOnly
# Create your views here.
class UserList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsUserOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
