# Generated by Django 3.2.4 on 2021-06-14 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210614_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='level',
            field=models.CharField(blank=True, choices=[(1, 'Foundation'), (2, 'Intermediate'), (3, 'Advanced'), (4, 'Expert')], max_length=255, null=True, verbose_name='Level'),
        ),
        migrations.DeleteModel(
            name='Skill_Levels',
        ),
    ]
