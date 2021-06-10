import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class ModelMixin(models.Model):
    id = models.UUIDField(
        _("ID"),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    created_at = models.DateTimeField(
        _("Created at"),
        auto_now_add=True,
        null=False,
        blank=False,
    )
    updated_at = models.DateTimeField(
        _("Updated at"),
        auto_now=True,
        null=True,
        blank=False,
    )
    deleted_at = models.DateTimeField(
        _("Deleted at"),
        null=True,
        blank=True, 
        )

    def __str__(self) -> str:
        return str(self.pk)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}<{self}>"

    class Meta:
        abstract = True