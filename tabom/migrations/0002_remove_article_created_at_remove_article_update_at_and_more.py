# Generated by Django 5.1.2 on 2024-10-16 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tabom", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="article",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="article",
            name="update_at",
        ),
        migrations.RemoveField(
            model_name="like",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="like",
            name="update_at",
        ),
        migrations.RemoveField(
            model_name="user",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="user",
            name="update_at",
        ),
    ]