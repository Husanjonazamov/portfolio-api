from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import CategoryModel, PortfolioModel, ResumeModel, SkilsModel
from ..serializers.portfolio import (
    CreateCategorySerializer,
    CreatePortfolioSerializer,
    CreateResumeSerializer,
    CreateSkilsSerializer,
    ListCategorySerializer,
    ListPortfolioSerializer,    
    ListResumeSerializer,
    ListSkilsSerializer,
    RetrieveCategorySerializer,
    RetrievePortfolioSerializer,
    RetrieveResumeSerializer,
    RetrieveSkilsSerializer,
)


@extend_schema(tags=["Category"])
class CategoryView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = CategoryModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListCategorySerializer
            case "retrieve":
                return RetrieveCategorySerializer
            case "create":
                return CreateCategorySerializer
            case _:
                return ListCategorySerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()


@extend_schema(tags=["Skils"])
class SkilsView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = SkilsModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListSkilsSerializer
            case "retrieve":
                return RetrieveSkilsSerializer
            case "create":
                return CreateSkilsSerializer
            case _:
                return ListSkilsSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()


@extend_schema(tags=["Portfolio"])
class PortfolioView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = PortfolioModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListPortfolioSerializer
            case "retrieve":
                return RetrievePortfolioSerializer
            case "create":
                return CreatePortfolioSerializer
            case _:
                return ListPortfolioSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()


@extend_schema(tags=["Resume"])
class ResumeView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = ResumeModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListResumeSerializer
            case "retrieve":
                return RetrieveResumeSerializer
            case "create":
                return CreateResumeSerializer
            case _:
                return ListResumeSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
