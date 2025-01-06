from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import BaseskilsModel
from ..serializers.baseskils import CreateBaseskilsSerializer, ListBaseskilsSerializer, RetrieveBaseskilsSerializer


@extend_schema(tags=["baseskils"])
class BaseskilsView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = BaseskilsModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListBaseskilsSerializer
            case "retrieve":
                return RetrieveBaseskilsSerializer
            case "create":
                return CreateBaseskilsSerializer
            case _:
                return ListBaseskilsSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
