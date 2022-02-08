# Generated by Django 4.0 on 2022-01-22 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_edge_map_alter_node_map'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='fontcolour',
            field=models.CharField(choices=[('blue', 'blue'), ('green', 'green'), ('red', 'red'), ('orange', 'orange'), ('black', 'black'), ('white', 'white')], default='white', max_length=255, null=True),
        ),
    ]
