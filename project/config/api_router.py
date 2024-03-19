from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from users.api.views import UserViewSet
from messanger import views

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"

urlpatterns = [
    path("chats/", views.ChatListAPIView.as_view()),
    path("messages/", views.MessageListAPIView.as_view()),
]

urlpatterns += router.urls
