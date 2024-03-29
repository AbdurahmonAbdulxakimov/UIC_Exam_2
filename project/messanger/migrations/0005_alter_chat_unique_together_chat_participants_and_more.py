# Generated by Django 4.2.7 on 2024-03-19 16:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("messanger", "0004_chat"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="chat",
            unique_together=set(),
        ),
        migrations.AddField(
            model_name="chat",
            name="participants",
            field=models.ManyToManyField(
                editable=False, related_name="chats", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.RemoveField(
            model_name="chat",
            name="user1",
        ),
        migrations.RemoveField(
            model_name="chat",
            name="user2",
        ),
    ]
