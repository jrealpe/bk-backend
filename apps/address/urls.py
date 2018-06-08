from django.conf.urls import include, url

from rest_framework import routers

from apps.address.viewsets import ProvinceViewSet, CityViewSet


router = routers.DefaultRouter()
router.register(r'provinces', ProvinceViewSet, base_name='province')
router.register(r'cities', CityViewSet, base_name='city')

urlpatterns = [
    url(r'^/', include(router.urls)),
]
