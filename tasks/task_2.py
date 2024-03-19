from django.db import models


class Vacancy(models.Model):
    title = models.CharField(max_length=255)

    salary_from = models.IntegerField(default=0)
    salary_to = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)


# ---------------------- SERIALIZER & VIEWS --------------------

from django_filters.rest_framework.filterset import FilterSet
import django_filters
from rest_framework.generics import ListAPIView

from vacancy.models import Vacancy
from vacancy.serializers import VacancySerializer


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = "__all__"


class VacancyFilter(FilterSet):
    class Meta:
        model = Vacancy
        fields = {
            "salary": ["range", "gte", "lte"],
            "salary_from": ["lte"],
            "salary_to": ["gte"],
        }


class VacancyListAPIView(ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

    filterset_class = VacancyFilter
