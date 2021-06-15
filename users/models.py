
from family_list_project.menagers.users import UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from family_list_project.mixins.model import ModelMixin


class User(AbstractBaseUser, PermissionsMixin, ModelMixin):
    username = models.CharField(
        _('Username'),
        max_length=150,
        unique=True,
    )
    email = models.EmailField(
        _("Email"), 
        unique=True
        )
    first_name = models.CharField(
        _("Name"), 
        max_length=50,
        )
    last_name = models.CharField(
        _("Name"), 
        max_length=50,
        )
    birthday = models.DateField(
        _("Birthday date"), 
        auto_now=False, 
        auto_now_add=False,
        blank=True,
        null=True,
        )
    date_joined = models.DateField(
        _("Birthday date"), 
        auto_now=False, 
        auto_now_add=False,
        blank=True,
        null=True,
        )
    gender = models.CharField(
        _("Gender"), 
        max_length=50
        )
    is_superuser = models.BooleanField(
        _('Is super user?'),
        default=False,
    )
    is_staff = models.BooleanField(
        _('Is staff?'),
        default=False,
    )
    is_active = models.BooleanField(
        _('Is active?'),
        default=True,
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["first_name"]

    def __str__(self) -> str:
        return self.username

