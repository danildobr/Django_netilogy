from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from  rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django_filters.rest_framework import DjangoFilterBackend, DateFromToRangeFilter
from rest_framework.filters import OrderingFilter

from advertisements.filters import AdvertisementFilter
from advertisements.permissions import IsOwnerReadOnly

class AdvertisementViewSet(ModelViewSet):
    '''ViewSet для объявлений.'''
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsOwnerReadOnly]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter  
    
    def get_permissions(self):
       if self.action in ['create', 'update', 'partial_update', 'destroy']:
           return [IsAuthenticated(), IsOwnerReadOnly()]
       return []
