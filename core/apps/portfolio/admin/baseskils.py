from django.contrib import admin

from ..models import BaseskilsModel
from unfold.admin import ModelAdmin


@admin.register(BaseskilsModel)
class BaseskilsAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
