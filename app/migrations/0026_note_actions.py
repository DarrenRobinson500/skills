# Generated by Django 4.0 on 2021-12-27 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_note_date_alter_note_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='actions',
            field=models.TextField(blank=True, null=True),
        ),
    ]
