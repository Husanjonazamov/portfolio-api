from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from ..models import ContactModel
from ..serializers.contact import CreateContactSerializer, ListContactSerializer, RetrieveContactSerializer


@extend_schema(tags=["contact"])
class ContactView(BaseViewSetMixin, ModelViewSet):
    queryset = ContactModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListContactSerializer
            case "retrieve":
                return RetrieveContactSerializer
            case "create":
                return CreateContactSerializer
            case _:
                return ListContactSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
