from datetime import datetime
from task_list.enums import TaskStatus
import uuid

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


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
    name = models.CharField(
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
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = "users"
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["name"]

    def __str__(self) -> str:
        return self.username



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



class Task(ModelMixin):
    name = models.CharField(
        _("Task name"), 
        max_length=50,
        )
    description = models.CharField(
        _("Task description"), 
        max_length=50,
        blank=True,
        null=True,
        )
    status =  models.CharField(
        _("Status"),
        max_length=10,
        choices=TaskStatus.choices,
        default=TaskStatus.CREATED,
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(
        User,
        verbose_name=_("Owner"),
        on_delete=models.PROTECT,
        blank=True, 
        null=True,
    )
    rating = models.IntegerField(
        _("Rating"), 
        null=True,
        blank=True,
        default=None
    )
    comments = models.CharField(
        _("Task comments"), 
        max_length=200,
        blank=True,
        null=True,
        )
    date = models.DateTimeField(
        _('data de criação'),
        default=datetime.utcnow(),
        blank=True,
        null=True,
        )

    def get_absolute_url(self):
        return reverse('task-update', kwargs={'pk': self.pk})


class Event(ModelMixin):
    name = models.CharField(
        _("Task name"), 
        max_length=50,
        )
    description = models.CharField(
        _("Task description"), 
        max_length=50,
        blank=True, 
        null=True,
        default=None
        )
    rating = models.IntegerField(
        _("Rating"), 
        null=True,
        blank=True, 
        default=None
    )
    start = models.DateField(
        _('Start date'),
        )
    finish = models.DateField(
        _('Finish date'),
        blank=True, 
        null=True,
        )
    tasks = models.ManyToManyField(
        Task,
        verbose_name=_("Tasks"),
        related_name="event"
    )
    # qtt_day
    # qtt_week
    # qtt_month
