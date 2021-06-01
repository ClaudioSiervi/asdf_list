import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class ModelMixin(models.Model):

    id = models.UUIDField(
        verbose_name=_("Id"),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created at"),
        auto_now_add=True,
        null=False,
        blank=False,
        help_text=_("Creation datetime"),
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated at"),
        auto_now=True,
        null=True,
        blank=False,
        help_text=_("Update datetime"),
    )
    deleted_at = models.DateTimeField(
        verbose_name=_("Deleted at"),
        null=True,
        blank=True, 
        help_text=_("Deletion datetime"),
        )

    def __str__(self):
        return str(self.pk)

    def __repr__(self):
        return f"{self.__class__.__name__}<{self}>"

    class Meta:
        abstract = True


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
        db_table = "users"
        verbose_name = _("Usuário")
        verbose_name_plural = _("Usuários")
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Family(ModelMixin):
    name = models.CharField(
        _("Nome grupo familiar"), 
        max_length=50,
        )
    members = models.ForeignKey(
        User, 
        verbose_name=_("Membros da família"), 
        on_delete=models.RESTRICT,    
    )

    class Meta:
        db_table = "families"
        verbose_name = _("Família")
        verbose_name_plural = _("Famílias")
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name 
