from django_filters import rest_framework as filters
from django_filters import FilterSet, DateFromToRangeFilter
from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['status', 'creator', 'created_at']
