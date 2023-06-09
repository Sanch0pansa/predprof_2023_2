# Generated by Django 4.1.7 on 2023-03-19 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_waypoint_day'),
    ]

    operations = [
        migrations.RenameField(
            model_name='waypoint',
            old_name='amount',
            new_name='SH',
        ),
        migrations.AlterField(
            model_name='day',
            name='waypoint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='API.waypoint'),
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nuclear_fuel', models.IntegerField()),
                ('oxygen', models.IntegerField()),
                ('nuclear_fuel_cost', models.IntegerField()),
                ('oxygen_cost', models.IntegerField()),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='API.day')),
            ],
        ),
    ]
