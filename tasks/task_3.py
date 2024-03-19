# ---------- renderers.py --------------------

import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from rest_framework.renderers import BaseRenderer
import json


# here the string gotten from the environmental variable is converted to bytes
AES_SECRET_KEY = "thisissomesecret"
AES_IV = reversed("thisissomesecret")


class AesRenderer(BaseRenderer):
    media_type = "application/octet-stream"
    format = "aes"

    def render(self, data, media_type=None, renderer_context=None):
        plaintext = json.dumps(data)
        padded_plaintext = pad(plaintext.encode(), 16)

        cipher = AES.new(AES_SECRET_KEY, AES.MODE_CBC, AES_IV)
        ciphertext = cipher.encrypt(padded_plaintext)
        ciphertext_b64 = base64.b64encode(ciphertext).decode()

        response = {"ciphertext": ciphertext_b64}

        return json.dumps(response)


# ------------- Models ------------------
from django.db import models


class Product(models.Model):
    price = models.DecimalField(decimal_places=2)
    marja = models.DecimalField(decimal_places=2)
    package_code = models.CharField(max_length=255)


# ------------- Serializers ----------------
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


# ------------- Views ------------------------------

from rest_framework.generics import ListAPIView


class ProductAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    renderer_classes = [AesRenderer]
