from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(
        self,
        request,
        view,
        obj
    ):
        # GET, HEAD, OPTIONS
        if request.method in SAFE_METHODS:
            return True

        return obj.user == request.user