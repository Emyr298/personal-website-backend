from rest_framework import permissions

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

class IsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or (request.user.is_superuser):
            return True
        return False