'''
Serializers for Product, Coupon and Offer Models
'''
from rest_framework import serializers

from apps.catalogue.models import Product, Coupon, Offer, Category


class ProductSerializer(serializers.ModelSerializer):
    """docstring for ProductSerializer"""
    class Meta:
        model = Product
        fields = ('id', 'title', 'image', 'description',)


class CouponSerializer(serializers.ModelSerializer):
    """docstring for CouponSerializer"""
    class Meta:
        model = Coupon
        fields = ('id', 'title', 'image',)


class OfferSerializer(serializers.ModelSerializer):
    """docstring for OfferSerializer"""
    class Meta:
        model = Offer
        fields = ('id', 'title', 'image',)
