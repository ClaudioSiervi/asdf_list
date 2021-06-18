# Generated by Django 3.2.4 on 2021-06-18 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('families', '0002_family_members'),
        ('event_list', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='family',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='families.family', verbose_name='Family'),
        ),
    ]