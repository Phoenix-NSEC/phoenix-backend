from rest_framework import permissions


class IsAdminOrWriteOnly(permissions.BasePermission):
    SAFE_METHODS = ["POST"]

    def has_permission(self, request, view):
        if request.method in self.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class IsAdminOrReadOnly(IsAdminOrWriteOnly):
    SAFE_METHODS = ["GET"]
