from rest_framework import serializers
from datetime import date

from apps.catalogue.models import Product, Coupon, Offer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'

class OfferSerializer(serializers.ModelSerializer):
	class Meta:
		model = Offer
		fields = '__all__'