from django.db import models

from django.utils.translation import gettext_lazy as _

from app.models.mixin import ModelMixin
from app.models.user import User


class Family(ModelMixin):
    name = models.CharField(
        _("Nome grupo familiar"), 
        max_length=50,
        )
    members = models.ForeignKey(
        User, 
        verbose_name=_("Membros da família"), 
        on_delete=models.RESTRICT, 
        related_name="family"   
    )

    class Meta:
        app_label = "family_list"
        db_table = "families"
        verbose_name = _("Família")
        verbose_name_plural = _("Famílias")
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name