# Generated by Django 3.2 on 2021-06-22 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20210622_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill_cat',
            name='to_develop',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]