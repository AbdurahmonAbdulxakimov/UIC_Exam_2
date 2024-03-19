from django.db import models
from django.contrib.auth import get_user_model

from utils.models import BaseModel
from common.models import Category

User = get_user_model()


class Company(BaseModel):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Vacany(BaseModel):
    title = models.CharField(max_length=255)

    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="vacancies"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="vacancies"
    )

    def __str__(self):
        return self.title
