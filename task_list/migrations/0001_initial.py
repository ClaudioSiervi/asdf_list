# Generated by Django 3.2.4 on 2021-06-24 23:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('families', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated at')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted at')),
                ('name', models.CharField(max_length=50, verbose_name='Task name')),
                ('description', models.CharField(blank=True, max_length=50, null=True, verbose_name='Task description')),
                ('status', models.CharField(blank=True, choices=[('CREATED', 'Created'), ('WAITING', 'Wating'), ('DONE', 'Done')], default='CREATED', max_length=10, null=True, verbose_name='Status')),
                ('rating', models.IntegerField(blank=True, default=None, null=True, verbose_name='Rating')),
                ('comments', models.CharField(blank=True, max_length=200, null=True, verbose_name='Task comments')),
                ('task_date_time', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Task date')),
                ('is_concluded', models.BooleanField(default=False, verbose_name='Is concluded?')),
                ('conclusion_date', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Task date')),
                ('family', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='families.family', verbose_name='Family')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
