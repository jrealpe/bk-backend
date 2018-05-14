from rest_framework import viewsets

from apps.catalogue.models import Product, Coupon, Offer
from apps.catalogue.serializers import ProductSerializer, CouponSerializer, OfferSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer


class CouponViewSet(viewsets.ModelViewSet):
    queryset= Coupon.objects.all()
    serializer_class = CouponSerializer

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
