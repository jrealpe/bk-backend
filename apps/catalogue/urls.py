from django.conf.urls import include, url

from rest_framework import routers

from apps.catalogue.viewsets import ProductViewSet, CouponViewSet


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, base_name='product')
router.register(r'coupons', CouponViewSet, base_name='coupon')

urlpatterns = [
	url(r'^/', include(router.urls)),
]
