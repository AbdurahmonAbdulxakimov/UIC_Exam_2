from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import (
    ContentType,
    GenericForeignKey,
    GenericRelation,
)

from utils.models import BaseModel


User = get_user_model()


class Message(BaseModel):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages_sent"
    )
    reciever = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages_received"
    )

    # content = models.TextField()

    content_type = models.ForeignKey(
        ContentType,
        limit_choices_to={"model__in": ("text", "video", "image", "file", "audio")},
        on_delete=models.CASCADE,
    )

    is_read = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.sender_id} - {self.reciever_id}"


class ObjectBase(models.Model):
    owner = models.ForeignKey(
        User, related_name="%(class)s_related", on_delete=models.CASCADE
    )
    model_content = models.ForeignKey(
        Message, on_delete=models.CASCADE, related_name="%(class)s_related"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Text(ObjectBase):
    content = models.TextField()


class Audio(ObjectBase):
    content = models.FileField(upload_to="audio")


class Image(ObjectBase):
    content = models.ImageField(upload_to="images")


class File(ObjectBase):
    content = models.FileField(upload_to="file")


class Chat(BaseModel):
    user1 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="owner_chats"
    )
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chats")

    class Meta:
        unique_together = ("user1", "user2")
