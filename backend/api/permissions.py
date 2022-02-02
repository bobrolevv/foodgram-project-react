from rest_framework import permissions


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):
    # code = 200

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.author == request.user:
            return True