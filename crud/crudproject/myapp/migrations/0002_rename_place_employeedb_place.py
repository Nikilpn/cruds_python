# Generated by Django 5.1.6 on 2025-02-28 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeedb',
            old_name='place',
            new_name='Place',
        ),
    ]
