from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # read permissions are allowed to any request
        # so we will always allow GET, HEAD, or OPTIONS requests

        if request.method in permissions.SAFE_METHODS:
            return True

        # write permissions are only allowed by the owner of the snippet
        return obj.owner == request.user
