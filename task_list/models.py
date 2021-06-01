import uuid

from django.db import models
from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

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


class User(AbstractBaseUser, PermissionsMixin, ModelMixin):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
    )
    email = models.EmailField(
        _("Email"), 
        unique=True
        )
    name = models.CharField(
        _("Nome"), 
        max_length=50,
        )
    birthday = models.DateField(
        _("Data aniversário"), 
        auto_now=False, 
        auto_now_add=False,
        blank=True,
        null=True,
        )
    gender = models.CharField(
        _("Gênero"), 
        max_length=50
        )
    is_superuser = models.BooleanField(
        _('É super usuário'),
        default=False,
    )
    is_staff = models.BooleanField(
        _('É da organização'),
        default=False,
    )
    is_active = models.BooleanField(
        _('ativo'),
        default=True,
    )


    objects = UserManager()
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
    members = models.ManyToManyField(
        User, 
        verbose_name=_("Membros da família"),    
        related_name='family',    
    )

    class Meta:
        db_table = "families"
        verbose_name = _("Família")
        verbose_name_plural = _("Famílias")
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name 
