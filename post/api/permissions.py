from rest_framework import permissions

class UserPermission(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        
        # Write permissions are only allowed to the owner of the snippet.
        return obj.id == request.user.id