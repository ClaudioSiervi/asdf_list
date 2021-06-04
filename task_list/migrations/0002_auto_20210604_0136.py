# Generated by Django 3.2.4 on 2021-06-04 01:36

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Task description'),
        ),
        migrations.AlterField(
            model_name='task',
            name='comments',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Task comments'),
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 4, 1, 36, 59, 682617), null=True, verbose_name='data de criação'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Task description'),
        ),
        migrations.AlterField(
            model_name='task',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('CREATED', 'Created'), ('WAITING', 'Wating'), ('DONE', 'Done')], default='CREATED', max_length=10, null=True, verbose_name='Status'),
        ),
    ]
