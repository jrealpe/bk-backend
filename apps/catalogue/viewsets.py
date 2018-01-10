from rest_framework import viewsets

from apps.catalogue.models import Product, Coupon
from apps.catalogue.serializers import ProductSerializer, CouponSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer


class CouponViewSet(viewsets.ModelViewSet):
    queryset= Coupon.objects.all()
    serializer_class = CouponSerializer
