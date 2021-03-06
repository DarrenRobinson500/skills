# Generated by Django 4.0 on 2022-01-21 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_note_time_changed_alter_note_status_alter_note_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mindmap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('size_x', models.IntegerField(null=True)),
                ('size_y', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255, null=True)),
                ('colour', models.CharField(choices=[('blue', 'blue'), ('green', 'green'), ('red', 'red'), ('orange', 'orange'), ('black', 'black'), ('white', 'white')], max_length=255, null=True)),
                ('shape', models.CharField(choices=[('rect', 'rect')], max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Edge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_a', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='start', to='app.node')),
                ('node_b', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='end', to='app.node')),
            ],
        ),
    ]
