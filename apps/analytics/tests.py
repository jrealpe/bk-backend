'''
Pruebas Unitarias para Estadísticas
Se crea un usuario, producto, oferta y cupón de prueba
'''
import tempfile
import datetime

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError, DataError
from django.test import TestCase
from django.test import override_settings

from PIL import Image

from apps.catalogue.models import *
from apps.analytics.models import *


User = get_user_model()


class AnalyticsTestCase(TestCase):

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def setUp(self):
        '''
        Objetos Temporales para pruebas
        '''
        self.tmp_img = tempfile.NamedTemporaryFile(suffix='.png')
        image = Image.new('RGB', (200, 200), (255, 0, 0))
        image.save(self.tmp_img, 'png')

        self.user = User.objects.create_user(
            username=settings.TEST_USERNAME,
            password=settings.TEST_PASSWORD
        )

        self.category = Category.objects.create(
            name='Dobles',
            image=self.tmp_img.name,
            created_user=self.user,
            modified_user=self.user
        )

        self.product = Product.objects.create(
            title='Papas Fritas',
            description='Acaramelada',
            category=self.category,
            image=self.tmp_img.name,
            created_user=self.user,
            modified_user=self.user
        )

        self.offer = Offer.objects.create(
            title='Oferta de Papas Fritas',
            description='Acaramelada',
            date_expiry=datetime.strptime('2020-10-1', '%Y-%m-%d'),
            created_user=self.user,
            modified_user=self.user
        )

        self.coupon = Coupon.objects.create(
            title='Cupón de Papas Fritas',
            description='Acaramelada',
            date_expiry=datetime.strptime('2020-10-1', '%Y-%m-%d'),
            created_user=self.user,
            modified_user=self.user
        )

    ########################
    # UserRecord Unit Test #
    ########################

    def test_user_record_create_cp001(self):
         '''
         Pruebas de Ingreso UserRecord exitoso
         '''
         user_record = UserRecord.objects.create(user=self.user)
         with self.assertRaises(AssertionError):
             with self.assertRaises(ValidationError):
                 user_record.full_clean()
 
    def test_user_record_create_cp001(self):
         '''
         Pruebas de Ingreso UserRecord sin usuario
         '''
         with self.assertRaises(IntegrityError):
             UserRecord.objects.create(user=None)

    ###########################
    # ProductRecord Unit Test #
    ###########################

    def test_product_record_create_cp001(self):
         '''
         Pruebas de Ingreso ProductRecord exitoso
         '''
         product_record = ProductRecord.objects.create(product=self.product)
         with self.assertRaises(AssertionError):
             with self.assertRaises(ValidationError):
                 product_record.full_clean()

    def test_product_record_create_cp001(self):
         '''
         Pruebas de Ingreso ProductRecord sin producto
         '''
         with self.assertRaises(IntegrityError):
             ProductRecord.objects.create(product=None)

    #############################
    # UserProductView Unit Test #
    #############################

    def test_user_product_view_create_cp001(self):
         '''
         Pruebas de Ingreso UserProductView exitoso
         '''
         user_product_view = UserProductView.objects.create(
             user=self.user,
             product=self.product)
         with self.assertRaises(AssertionError):
             with self.assertRaises(ValidationError):
                 user_product_view.full_clean()

    def test_user_product_view_create_cp001(self):
         '''
         Pruebas de Ingreso UserProductView sin usuario
         '''
         with self.assertRaises(IntegrityError):
             UserProductView.objects.create(user=None, product=self.product)

    def test_user_product_view_create_cp001(self):
         '''
         Pruebas de Ingreso UserProductView sin producto
         '''
         with self.assertRaises(IntegrityError):
             UserProductView.objects.create(user=self.user, product=None)

    ##########################
    # CouponRecord Unit Test #
    ##########################

    def test_coupon_record_create_cp001(self):
         '''
         Pruebas de Ingreso CouponRecord exitoso
         '''
         coupon_record = CouponRecord.objects.create(coupon=self.coupon)
         with self.assertRaises(AssertionError):
             with self.assertRaises(ValidationError):
                 coupon_record.full_clean()

    def test_coupon_record_create_cp001(self):
         '''
         Pruebas de Ingreso CouponRecord sin cupón
         '''
         with self.assertRaises(IntegrityError):
             CouponRecord.objects.create(coupon=None)

    ############################
    # UserCouponView Unit Test #
    ############################

    def test_user_coupon_view_create_cp001(self):
         '''
         Pruebas de Ingreso UserCouponView exitoso
         '''
         user_coupon_view = UserCouponView.objects.create(
             user=self.user,
             coupon=self.coupon)
         with self.assertRaises(AssertionError):
             with self.assertRaises(ValidationError):
                 user_coupon_view.full_clean()

    def test_user_coupon_view_create_cp001(self):
         '''
         Pruebas de Ingreso UserCouponView sin usuario
         '''
         with self.assertRaises(IntegrityError):
             UserCouponView.objects.create(user=None, coupon=self.coupon)

    def test_user_coupon_view_create_cp001(self):
         '''
         Pruebas de Ingreso UserCouponView sin cupón
         '''
         with self.assertRaises(IntegrityError):
             UserCouponView.objects.create(user=self.user, coupon=None)

    #########################
    # OfferRecord Unit Test #
    #########################

    def test_offer_record_create_cp001(self):
         '''
         Pruebas de Ingreso OfferRecord exitoso
         '''
         offer_record = OfferRecord.objects.create(offer=self.offer)
         with self.assertRaises(AssertionError):
             with self.assertRaises(ValidationError):
                 offer_record.full_clean()

    def test_offer_record_create_cp001(self):
         '''
         Pruebas de Ingreso OfferRecord sin oferta
         '''
         with self.assertRaises(IntegrityError):
             OfferRecord.objects.create(offer=None)

    ###########################
    # UserOfferView Unit Test #
    ###########################

    def test_user_offer_view_create_cp001(self):
         '''
         Pruebas de Ingreso UserOfferView exitoso
         '''
         user_offer_view = UserOfferView.objects.create(
             user=self.user,
             offer=self.offer)
         with self.assertRaises(AssertionError):
             with self.assertRaises(ValidationError):
                 user_coupon_view.full_clean()

    def test_user_offer_view_create_cp001(self):
         '''
         Pruebas de Ingreso UserOfferView sin usuario
         '''
         with self.assertRaises(IntegrityError):
             UserOfferView.objects.create(user=None, offer=self.offer)

    def test_user_offer_view_create_cp001(self):
         '''
         Pruebas de Ingreso UserOfferView sin oferta
         '''
         with self.assertRaises(IntegrityError):
             UserOfferView.objects.create(user=self.user, offer=None)
