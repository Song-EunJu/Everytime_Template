# Generated by Django 4.0.4 on 2022-05-24 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EverytimeApp', '0007_alter_board_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='comments',
        ),
    ]
