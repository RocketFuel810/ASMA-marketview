# Generated by Django 5.0.6 on 2024-06-24 13:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("marketview", "0004_newslist_summary"),
    ]

    operations = [
        migrations.CreateModel(
            name="NewsTopic",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("topic", models.CharField(max_length=30)),
            ],
        ),
    ]
