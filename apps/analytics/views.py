from django.shortcuts import render, get_object_or_404

from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response

from apps.catalogue.models import *

from .models import *


@api_view(['POST'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def product_record(request, pk=None):
    '''
    Product Record
    '''
    try:
        user = request.user
        product = get_object_or_404(Product, pk=pk)
        user_product_view, created = UserProductView.objects.get_or_create(
            user=user,
            product=product)

        if created:
            user_record, created = UserRecord.objects.get_or_create(
                user=user)
            user_record.num_product_views += 1
            user_record.save()
         
            product_record, created = ProductRecord.objects.get_or_create(
                product=product)
            product_record.num_views += 1
            product_record.save()

        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def coupon_record(request, pk=None):
    '''
    Coupon Record
    '''
    try:
        user = request.user
        coupon = get_object_or_404(Coupon, pk=pk)
        user_coupon_view, created = UserCouponView.objects.get_or_create(
            user=user,
            coupon=coupon)

        if created:
            user_record, created = UserRecord.objects.get_or_create(
                user=user)
            user_record.num_coupon_views += 1
            user_record.save()
         
            coupon_record, created = CouponRecord.objects.get_or_create(
                coupon=coupon)
            coupon_record.num_views += 1
            coupon_record.save()

        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes((TokenAuthentication, ))
@permission_classes((IsAuthenticated, ))
def offer_record(request, pk=None):
    '''
    Offer Record
    '''
    try:
        user = request.user
        offer = get_object_or_404(Offer, pk=pk)
        user_offer_view, created = UserOfferView.objects.get_or_create(
            user=user,
            offer=offer)

        if created:
            user_record, created = UserRecord.objects.get_or_create(
                user=user)
            user_record.num_offer_views += 1
            user_record.save()
         
            offer_record, created = OfferRecord.objects.get_or_create(
                offer=offer)
            offer_record.num_views += 1
            offer_record.save()

        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
