from django.conf.urls import include, url

from rest_framework import routers

from .views import *


urlpatterns = [
    url(r'^product/(?P<pk>\d+)/$', product_record),
    url(r'^coupon/(?P<pk>\d+)/$', coupon_record),
    url(r'^offer/(?P<pk>\d+)/$', offer_record),
]
