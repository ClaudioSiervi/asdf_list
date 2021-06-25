# Generated by Django 3.2.4 on 2021-06-24 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event_list', '0001_initial'),
        ('families', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='family',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='families.family', verbose_name='Family'),
        ),
    ]
