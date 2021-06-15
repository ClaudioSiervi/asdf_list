from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from family_list_project.mixins.model import ModelMixin
from task_list.enums import TaskStatus
from users.models import User


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
    task_date_time = models.DateTimeField(
        _('Task date'),
        default=None,
        blank=True,
        null=True,
        )
    is_concluded = models.BooleanField(
        _('Is concluded?'),
        default=False,
    )
    conclusion_date = models.DateTimeField(
        _('Task date'),
        default=None,
        blank=True,
        null=True,
        )

    def get_absolute_url(self):
        return reverse('task-update', kwargs={'pk': self.pk})
