'''
ViewSets for Address's Province and City
'''
from rest_framework import viewsets

from apps.address.models import Province, City
from apps.address.serializers import ProvinceSerializer, CitySerializer


class ProvinceViewSet(viewsets.ModelViewSet):
    '''
    A ViewSet for listing provinces
    '''
    queryset = Province.objects.all()    
    serializer_class = ProvinceSerializer


class CityViewSet(viewsets.ModelViewSet):
    '''
    A ViewSet for listing cities
    '''
    queryset = City.objects.all()    
    serializer_class = CitySerializer
    filter_fields = ('province',)
    ordering = ('name',)
