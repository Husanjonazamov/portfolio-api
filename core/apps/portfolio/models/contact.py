from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class ContactModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)
    subject = models.CharField(_('subject'), max_length=100)
    message = models.TextField(_('message'))

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "contact"
        verbose_name = _("ContactModel")
        verbose_name_plural = _("ContactModels")
