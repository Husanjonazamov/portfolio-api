from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class CategoryModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Category"
        verbose_name = _("CategoryModel")
        verbose_name_plural = _("CategoryModels")


class SkilsModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Skils"
        verbose_name = _("SkilsModel")
        verbose_name_plural = _("SkilsModels")


class PortfolioModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    skils = models.ManyToManyField(SkilsModel)
    image = models.ImageField(upload_to='portfolio_image/')
    description = models.TextField()
    git_url = models.CharField(max_length=255)
    project_url = models.CharField(max_length=255) 
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Portfolio"
        verbose_name = _("PortfolioModel")
        verbose_name_plural = _("PortfolioModels")


class ResumeModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)
    resume = models.FileField(upload_to='resume/')

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "Resume"
        verbose_name = _("ResumeModel")
        verbose_name_plural = _("ResumeModels")
