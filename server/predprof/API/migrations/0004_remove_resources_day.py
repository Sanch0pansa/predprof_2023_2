# Generated by Django 4.1.7 on 2023-03-19 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_rename_amount_waypoint_sh_alter_day_waypoint_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resources',
            name='day',
        ),
    ]