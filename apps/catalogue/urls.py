'''
Se define las rutas
'''
from django.conf.urls import include, url

from rest_framework import routers

from apps.catalogue.viewsets import ProductViewSet, CouponViewSet, OfferViewSet


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, base_name='product')
router.register(r'coupons', CouponViewSet, base_name='coupon')
router.register(r'offers', OfferViewSet, base_name='offer')

urlpatterns = [
    url(r'^/', include(router.urls)),
]
