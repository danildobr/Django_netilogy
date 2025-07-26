from rest_framework.permissions import BasePermission


class IsOwnerReadOnly(BasePermission):
    """Разрешение, позволяющее только владельцу объекта редактировать/удалять его."""
    def has_object_permission(self, request, view, obj):
       # Разрешаем чтение (GET, HEAD, OPTIONS) для всех
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
           return True
        # Разрешаем запись только владельцу объявления
        return obj.creator == request.user
   