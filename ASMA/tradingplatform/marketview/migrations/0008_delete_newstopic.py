# Generated by Django 5.0.6 on 2024-06-26 06:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("marketview", "0007_newslist_link"),
    ]

    operations = [
        migrations.DeleteModel(
            name="NewsTopic",
        ),
    ]
