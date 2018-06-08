'''
ViewSets for Catalogue's Offers, Coupons and Products
'''
from rest_framework import viewsets
from rest_framework.response import Response

from apps.catalogue.models import Product, Coupon, Offer, Category
from apps.catalogue.serializers import ProductSerializer, CouponSerializer, OfferSerializer


class ProductViewSet(viewsets.ViewSet):
    '''
    A ViewSet for listing products
    '''
    def get_products(self, pk):
        queryset = Product.objects.all().filter(category=pk)
        serializer_class = ProductSerializer(queryset, many=True)
        return serializer_class.data

    def list(self, request):
        queryset_category = Category.objects.all()
        queryset_filter = {}
        queryset = []
        for category in queryset_category:
            serializer_product = self.get_products(category.id)
            queryset_filter[category.name] = serializer_product
            queryset.append(queryset_filter) 
        return Response(queryset[0])


class CouponViewSet(viewsets.ViewSet):
    '''
    A ViewSet for listing coupons
    '''
    def list(self, request):
        '''Returns serialized class response from Coupon'''
        queryset = Coupon.objects.all()
        queryset_filter = []
        for coupon in queryset:
            if coupon.is_past_due:
                queryset_filter.append(coupon)
        serializer_class = CouponSerializer(queryset_filter, many=True)
        return Response(serializer_class.data)


class OfferViewSet(viewsets.ViewSet):
    '''
    A ViewSet for listing offers
    '''
    def list(self, request):
        '''Returns serialized class response from Offer'''
        queryset = Offer.objects.all()
        queryset_filter = []
        for offer in queryset:
            if offer.is_past_due:
                queryset_filter.append(offer)
        serializer_class = OfferSerializer(queryset_filter, many=True)
        return Response(serializer_class.data)
