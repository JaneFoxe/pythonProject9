from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    """Проверка, входит ли пользователь в группу moderator."""
    message = 'Adding customers not allowed.'

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moderator").exists()


class IsOwner(permissions.BasePermission):
    """Проверка, является ли пользователь владельцем."""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
