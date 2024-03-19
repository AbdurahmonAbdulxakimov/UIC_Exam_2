from rest_framework import generics
from django.db.models import Q

from messanger import models, serializers


class MessageListAPIView(generics.ListAPIView):
    queryset = models.Message.objects.all().select_related(
        "content_type", "sender", "reciever"
    )
    serializer_class = serializers.MessageSerializer

    def get_queryset(self):
        qs = (
            super()
            .get_queryset()
            .filter(Q(sender=self.request.user) | Q(reciever=self.request.user))
        )
        return qs[:20]


class ChatListAPIView(generics.ListAPIView):
    queryset = models.Message.objects.all().select_related(
        "content_type", "sender", "reciever"
    )
    serializer_class = serializers.ChatSerializer

    def get_queryset(self):
        qs = (
            super()
            .get_queryset()
            .filter(Q(sender=self.request.user) | Q(reciever=self.request.user))
            .values("sender", "reciever")
            .distinct()
        )
        return qs
