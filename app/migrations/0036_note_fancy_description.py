# Generated by Django 4.0 on 2022-02-08 04:47

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_node_description_alter_edge_map_alter_edge_node_a_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='fancy_description',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
