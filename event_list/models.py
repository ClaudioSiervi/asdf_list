from django.db import models
from django.utils.translation import gettext_lazy as _

from family_list_project.mixins.model import ModelMixin
from task_list.models import Task, User


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
        null=True,
        blank=True, 
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
    owner = models.ForeignKey(
        User,
        verbose_name=_("Owner"),
        on_delete=models.PROTECT,
        blank=True, 
        null=True,
    )
