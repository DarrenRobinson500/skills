# Generated by Django 3.2.4 on 2021-06-18 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210618_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill_cat',
            name='score1',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='skill_cat',
            name='score2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='skill_cat',
            name='score3',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='skill_cat',
            name='score4',
            field=models.FloatField(null=True),
        ),
    ]
