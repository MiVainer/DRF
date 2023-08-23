# -------------------------#
# ---Program by MiVainer---#
from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: #Если запрос безопасный (GET, HEAD, OPTIONS) , предоставляем права доступа всем
            return True #True - права предоставлены, False - не предоставлены

        return bool(request.user and request.user.is_staff) # Если запрос не безопасный, даём доступ только для админа


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Просматривать может любой, а удалять только тот кто добавил
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user #Если пользователь из БД такой же как пользователь создавший запрос, возвращаем True