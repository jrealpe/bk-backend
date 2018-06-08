'''
Serializers for Province and City Models
'''
from rest_framework import serializers

from apps.address.models import Province, City


class ProvinceSerializer(serializers.ModelSerializer):
    """docstring for ProvinceSerializer"""

    class Meta:
        model = Province
        fields = ('id', 'name')


class CitySerializer(serializers.ModelSerializer):
    """docstring for CitySerializer"""

    class Meta:
        model = City
        fields = ('id', 'name')
