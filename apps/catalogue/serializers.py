from rest_framework import serializers
from datetime import date

from apps.catalogue.models import Product, Coupon


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CouponSerializer(serializers.ModelSerializer):

    date_expiry = serializers.DateTimeField()

    def validate_date_expiry(self, value):
        """
        """
        if date.today > value:
            raise serializers.ValidationError("Fecha pasada")
        return value

    class Meta:
        model = Coupon
        fields = ('date_expiry')
