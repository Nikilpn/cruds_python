# Generated by Django 5.1.3 on 2024-11-23 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empapp', '0003_rename_studentdb_employeedb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedb',
            name='PLACE',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]