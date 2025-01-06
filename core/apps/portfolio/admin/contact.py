from django.contrib import admin

from ..models import ContactModel
from unfold.admin import ModelAdmin


@admin.register(ContactModel)
class ContactAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
