# Generated by Django 4.2.7 on 2024-03-19 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0001_initial"),
        ("users", "0003_alter_user_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="users",
                to="common.category",
            ),
        ),
    ]