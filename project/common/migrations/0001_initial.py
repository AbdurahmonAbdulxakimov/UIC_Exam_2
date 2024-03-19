# Generated by Django 4.2.7 on 2024-03-19 08:01

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255, unique=True)),
                ("avg_salary", models.PositiveBigIntegerField(default=0)),
                ("users_count", models.PositiveIntegerField(default=0)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]