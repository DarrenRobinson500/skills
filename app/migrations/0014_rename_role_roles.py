# Generated by Django 3.2 on 2021-06-22 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_rename_roles_role'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Role',
            new_name='Roles',
        ),
    ]
