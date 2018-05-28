'''
Vistas del controlador
'''
from rest_framework import viewsets

from apps.catalogue.models import Product, Coupon, Offer
from apps.catalogue.serializers import ProductSerializer, CouponSerializer, OfferSerializer


class ProductViewSet(viewsets.ModelViewSet):
    '''
    Vistas de los productos
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CouponViewSet(viewsets.ModelViewSet):
    '''
    Vistas de cupones
    '''
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class OfferViewSet(viewsets.ModelViewSet):
    '''
    Vistas de ofertas
    '''
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
