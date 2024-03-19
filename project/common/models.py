from django.db import models

from utils.models import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=255, unique=True)

    avg_salary = models.PositiveBigIntegerField(default=0)
    users_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
