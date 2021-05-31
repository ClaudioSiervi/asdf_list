from django.db import models

from django.utils.translation import gettext_lazy as _

from app.models.mixin import ModelMixin


class User(ModelMixin):
    name = models.CharField(
        _("Nome"), 
        max_length=50,
        )
    birthday = models.DateField(
        _("Data aniversário"), 
        auto_now=False, 
        auto_now_add=False,
        )
    gender = models.CharField(
        _("Gênero"), 
        max_length=50
        )
    
    class Meta:
        app_label = "family_list"
        db_table = "users"
        verbose_name = _("Usuário")
        verbose_name_plural = _("Usuários")
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name
