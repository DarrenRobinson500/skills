# Generated by Django 3.2 on 2021-06-22 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20210622_1952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role_level',
            old_name='role',
            new_name='role_level',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='level',
        ),
        migrations.AddField(
            model_name='skill',
            name='role_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.role_level'),
        ),
    ]
