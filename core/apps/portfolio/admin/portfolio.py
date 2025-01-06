from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import CategoryModel, PortfolioModel, ResumeModel, SkilsModel


@admin.register(CategoryModel)
class CategoryAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(SkilsModel)
class SkilsAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(PortfolioModel)
class PortfolioAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(ResumeModel)
class ResumeAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
