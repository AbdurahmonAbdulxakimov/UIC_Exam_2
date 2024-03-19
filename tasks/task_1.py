from django.db import models
from django.db.models import BaseManager, Manager


class BaseModelManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=False)

    objects_all = BaseManager()
    objects = BaseModelManager()

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    class Meta:
        abstract = True


class User(BaseModel):
    username = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.username


# ------------- Serializer ----------------
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("is_deleted",)


# ------------- VIEW ----------------------
from rest_framework.generics import CreateAPIView
from rest_framework.exceptions import AuthenticationFailed
from django.db.models import Q


class SignupView(CreateAPIView):
    queryset = User.objects_all.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        qs = self.get_queryset().filter(username=serializer.username)

        if qs.filter(is_deleted=False):
            raise AuthenticationFailed(
                detail="User already exists!",
            )

        if qs:
            qs[0].delete()

        return super().perform_create(serializer)


# --------------- LOGIN -----------------

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        if not user.is_deleted:
            return token

        raise AuthenticationFailed(
            detail="User deleted!",
        )


# Django project settings.py
SIMPLE_JWT = {
    "TOKEN_OBTAIN_SERIALIZER": "my_app.serializers.MyTokenObtainPairSerializer",
}
