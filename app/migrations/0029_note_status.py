# Generated by Django 4.0 on 2021-12-27 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_alter_note_time_stamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='status',
            field=models.TextField(blank=True, choices=[('Open', 'Open'), ('Complete', 'Complete')], null=True),
        ),
    ]
