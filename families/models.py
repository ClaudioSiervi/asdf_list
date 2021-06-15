from django.db import models
from django.utils.translation import gettext_lazy as _

from family_list_project.mixins.model import ModelMixin
from users.models import User


class Family(ModelMixin):
    name = models.CharField(
        _("Family denomination"), 
        max_length=50,
        )
    members = models.ManyToManyField(
        User, 
        verbose_name=_("Family members"),    
        related_name='family',    
    )

    class Meta:
        db_table = "families"
        verbose_name = _("Family")
        verbose_name_plural = _("Families")
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name 


