from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class BaseskilsModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)
    baseskils_icon = models.CharField(_('baseskils'), max_length=100)

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "baseskils"
        verbose_name = _("BaseskilsModel")
        verbose_name_plural = _("BaseskilsModels")
