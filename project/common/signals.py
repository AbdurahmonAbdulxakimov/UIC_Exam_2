from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import F, Min, Max
from django.contrib.auth import get_user_model

from common.models import Category


User = get_user_model()


@receiver(post_save, sender=User)
def category_cange(sender, instance, created, **kwargs) -> None:
    category = instance.category

    if created:
        # category.users_count += 1
        pass
    else:
        min_salary = (
            category.users.all().aggregate(Min("salary_exp")).get("salary_exp__min")
        )
        max_salary = (
            category.users.all().aggregate(Max("salary_exp")).get("salary_exp__max")
        )
        avg_salary = (max_salary + min_salary) / 2

        if max_salary / min_salary < 2:
            category.avg_salary = avg_salary
        else:
            category.avg_salary = (max_salary + avg_salary) / 2 - (
                avg_salary + min_salary
            ) / 2

        category.save()
