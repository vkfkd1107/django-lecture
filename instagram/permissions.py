from rest_framework import permissions


class IsAuthorOrReadonly(permissions.BasePermission):
    def pas_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permissions(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.author == request.user
