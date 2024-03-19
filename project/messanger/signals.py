from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import F, Min, Max, Q


from messanger.models import Message, Chat


@receiver(post_save, sender=Message)
def category_cange(sender, instance, created, **kwargs) -> None:

    if not Chat.objects.filter(
        Q(user1=instance.sender) & Q(user2=instance.reciever)
    ) or not Chat.objects.filter(Q(user1=instance.reciever) & Q(user2=instance.sender)):
        Chat.objects.create(user1=instance.sender, user2=instance.reciever)
