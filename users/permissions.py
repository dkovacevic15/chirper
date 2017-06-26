from rest_framework import permissions
from django.contrib.auth.models import User

class IsUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj == request.user or request.user.is_staff

class GetOrPostOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in ['GET', 'POST']:
            return True
        else:
            return False