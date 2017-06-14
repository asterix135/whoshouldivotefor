from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only owners of an object to edit it
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request,
        # so always allow GET, HEAD or OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        # limit write permissions to object creator
        return obj.creator == request.user
