# Generated by Django 3.2.4 on 2021-06-10 01:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_list', '0003_alter_task_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 10, 1, 22, 42, 473782), null=True, verbose_name='Task date'),
        ),
    ]
