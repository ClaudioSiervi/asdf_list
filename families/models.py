import enum

from django.db import models
from django.forms.fields import MultipleChoiceField
from django.utils.translation import gettext_lazy as _

from family_list_project.mixins.model import ModelMixin
from users.models import User


class FamilyInviteStatus(models.TextChoices, enum.Enum):
    CREATED = "CREATED", _("Created")
    ACCEPTED = "ACCEPTED", _("Accepted")
    DECLINED = "DECLINED", _("Declined")

    
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


class FamilyInvite(ModelMixin):
    family = models.ForeignKey(
        to=Family, 
        on_delete=models.RESTRICT,
        related_name="invites"
    )
    guest_name = models.CharField(
        _("Guest name"), 
        max_length=50,
    )
    guest_email = models.EmailField(
        _("Guest email"), 
        unique=True
    )
    status = models.CharField(
        _("Status"),
        max_length=15,
        choices=FamilyInviteStatus.choices,
        default=FamilyInviteStatus.CREATED,
    )
