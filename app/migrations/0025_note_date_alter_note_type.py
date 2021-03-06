# Generated by Django 4.0 on 2021-12-27 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_note_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='type',
            field=models.CharField(choices=[('Person', 'Person'), ('Objective', 'Objective'), ('Story', 'Story'), ('Issue', 'Issue'), ('To Do', 'To Do'), ('Group', 'Group'), ('Reminder', 'Reminder'), ('Meeting', 'Meeting')], max_length=64, null=True),
        ),
    ]
