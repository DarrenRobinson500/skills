import django_filters
from .models import *

class PeopleFilter(django_filters.FilterSet):
    class Meta:
        model = People
        fields = ("name", "role", )
