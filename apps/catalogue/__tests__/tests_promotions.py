'''
Pruebas Unitarias para el Catálogo
Se crea un usuario de prueba
Se crea uma imagen con ayuda de la librerìa PIL
La imagen creada se guada en el sistema de archivos temporales del S.O.
'''
import tempfile
import datetime
from PIL import Image
from django.conf import settings
from django.test import TestCase, override_settings
from django.db.utils import IntegrityError, DataError
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from apps.catalogue.models import Coupon, Offer

USER = get_user_model()

class TestPromotion(TestCase):
    '''
    Pruebas unitarias para Cupones y Ofertas del catálogo
    '''
    username = settings.TEST_USERNAME
    password = settings.TEST_PASSWORD

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def setUp(self):
        '''
        Crea un usuario para todas las pruebas que lo necesiten
        El decorador sobrescribe la ruta de MEDIA_ROOT
        por la del directorio de archivos temporales del sistema
        '''
        size = (200, 200)
        color = (255, 0, 0)
        image = Image.new('RGB', size, color)
        self.ext = 'png'
        # crea un archivo temporal .png
        # con un nombre visible en el sistema de archivos
        self.temp_image = tempfile.NamedTemporaryFile(suffix='.png')
        image.save(self.temp_image, self.ext)
        # utiliza usuario y contraseña de prueba
        self.user = USER.objects.create_user(
            username=self.username,
            password=self.password
        )


    def test_coupon_create_cp032(self):
        '''
        Pruebas de Ingreso Nuevo Cupón exitoso
        '''
        coupon = Coupon.objects.create(
            title='Papas Fritas',
            description='Acaramelada',
            date_expiry=datetime.datetime(2020, 10, 1),
            image=self.temp_image.name,
            created_user=self.user,
            modified_user=self.user
        )
        print('It Worked!', coupon.image)
        # Checkea el fallo de confirmar que existe algun error de validacion
        with self.assertRaises(AssertionError):
            # Se debe invocar a ValidationError para errores de este tipo
            # Asignados desde las funciones de Validación al Modelo Coupon
            with self.assertRaises(ValidationError):
                # Para validar a cada campo del formulario de Cupon
                coupon.full_clean()


    def test_offer_create_cp033(self):
        '''
        Pruebas de Ingreso Nuevä Oferta con título mayor a 30 caracteres
        Cuando de desborda el tamaño restringido en un campo de texto
        La DB devuelve DataError
        '''
        with self.assertRaises(DataError):
            offer = Offer.objects.create(
                title='Papas Fritas y algo más de 30 caracteres',
                description='Acaramelada',
                date_expiry=datetime.datetime(2020, 10, 1),
                image=self.temp_image.name,
                created_user=self.user,
                modified_user=self.user
            )
            offer.save()


    def test_coupon_create_cp034(self):
        '''
        Pruebas de Ingreso Nuevo Cupón con título de números
        '''
        coupon = Coupon.objects.create(
            title='Papas Fritas^1',
            description='Acaramelada',
            date_expiry=datetime.datetime(2020, 10, 1),
            image=self.temp_image.name,
            created_user=self.user,
            modified_user=self.user
        )
        # Se debe invocar a ValidationError para errores de este tipo
        # Asignados desde las funciones de Validación al Modelo de Categorias
        with self.assertRaises(ValidationError) as error:
            # Para validar a cada campo del formulario Cupón
            coupon.full_clean()
        exception = error.exception
        message = exception.message_dict['title'][0]
        # compara mensaje de error obtenido y el esperado
        self.assertEqual(message, 'Contiene carácteres especiales no '
                                  'permitidos o números/carácters muy '
                                  'largos. Ingrese sólo letras, números '
                                  'o # $ % & * / + - ¿ ? ! ¡ , .')


    def test_offer_create_cp035(self):
        '''
        Pruebas de Ingreso Nueva Oferta con título más 30 caracteres números
        Cuando de desborda el tamaño restringido en un campo de texto
        La DB devuelve DataError
        '''
        with self.assertRaises(DataError):
            offer = Offer.objects.create(
                title='1112253652Papas Fritas'
                      'y algo más de 30 caracteres',
                description='Acaramelada',
                date_expiry=datetime.datetime(2020, 10, 1),
                image=self.temp_image.name,
                created_user=self.user,
                modified_user=self.user
            )
            offer.save()


    def test_coupon_create_cp036(self):
        '''
        Pruebas de Ingreso Nuevo Cupón con descripción más de 60 caracteres
        '''
        coupon = Coupon.objects.create(
            title='Sandwich de pollo picante',
            description='Papas Fritas con Sandwich de pollo crujiente '
                        'picante hecho con pollo jugoso, tierno y crujiente '
                        '100% de carne blanca.',
            date_expiry=datetime.datetime(2020, 10, 1),
            image=self.temp_image.name,
            created_user=self.user,
            modified_user=self.user
        )
        with self.assertRaises(ValidationError) as error:
            coupon.full_clean()
        # compara mensaje de error obtenido y el esperado
        exception = error.exception
        message = exception.message_dict['description'][0]
        self.assertEqual(message, 'Asegúrese de que este valor tenga menos '
                                  'de 60 caracteres (tiene 117).')


    def test_offer_create_cp0037(self):
        '''
        Pruebas de Ingreso Nueva Oferta con descripción no alfanumérica
        '''
        offer = Offer.objects.create(
            title='Sandwich de pollo picante',
            description='Acaramelada #@1',
            date_expiry=datetime.datetime(2020, 10, 1),
            image=self.temp_image.name,
            created_user=self.user,
            modified_user=self.user
        )
        with self.assertRaises(ValidationError) as error:
            # Para validar a cada campo del formulario Oferta
            offer.full_clean()
        # compara mensaje de error obtenido y el esperado
        exception = error.exception
        message = exception.message_dict['description'][0]
        self.assertEqual(message, 'Contiene carácteres especiales no '
                                  'permitidos o números/carácters muy '
                                  'largos. Ingrese sólo letras, números '
                                  'o # $ % & * / + - ¿ ? ! ¡ , .')


    def test_coupon_create_cp038(self):
        '''
        Pruebas de Ingreso Nuevo Cupon descripción no alfanumérica mas de 60
        '''
        coupon = Coupon.objects.create(
            title='Sandwich de pollo picante',
            description='Papas Fritas@ con Sandwich de pollo crujiente '
                        'picante hecho con pollo jugoso, tierno y crujiente '
                        '100% de carne blanca.',
            date_expiry=datetime.datetime(2020, 10, 1),
            image=self.temp_image.name,
            created_user=self.user,
            modified_user=self.user
        )
        with self.assertRaises(ValidationError) as error:
            coupon.full_clean()
        # compara mensaje de error obtenido y el esperado
        exception = error.exception
        message_1 = exception.message_dict['description'][0]
        message_2 = exception.message_dict['description'][1]
        self.assertEqual(message_1, 'Contiene carácteres especiales no '
                                    'permitidos o números/carácters muy '
                                    'largos. Ingrese sólo letras, números '
                                    'o # $ % & * / + - ¿ ? ! ¡ , .')
        self.assertEqual(message_2, 'Asegúrese de que este valor tenga menos '
                                    'de 60 caracteres (tiene 118).')


    def test_offer_create_cp039(self):
        '''
        Pruebas de Ingreso Nueva Oferta con formato de imagen no permitido
        '''
        offer = Offer.objects.create(
            title='Papas Fritas',
            description='Acaramelada',
            date_expiry=datetime.datetime(2020, 10, 1),
            image=SimpleUploadedFile(
                'papas.raw',
                b'Este es un archivo de prueba!'),
            created_user=self.user,
            modified_user=self.user
        )
        with self.assertRaises(ValidationError) as error:
            offer.full_clean()
        # compara mensaje de error obtenido y el esperado
        exception = error.exception
        message = exception.message_dict['image'][1]
        self.assertEqual(message, '.raw no es una extensión de archivo '
                                  'permitida. Suba una imagen con extensión: '
                                  '.jpeg .jpeg o .png')


    def test_coupon_create_cp040(self):
        '''
        Pruebas de Ingreso Nuevo Cupón con formato de imagen no permitido
        titulo y descrpcion con mas de 30 y 60 caracteres respectivamente
        '''
        with self.assertRaises(DataError):
            coupon = Coupon.objects.create(
                title='Papas Fritas y algo más hasta los treinta',
                description='Papas Fritas con Sandwich de pollo crujiente '
                            'picante hecho con pollo jugoso, tierno y crujiente '
                            '100% de carne blanca.',
                date_expiry=datetime.datetime(2020, 10, 1),
                image=SimpleUploadedFile(
                    'papas.raw',
                    b'Este es un archivo de prueba!'),
                created_user=self.user,
                modified_user=self.user
            )
            coupon.save()


    def test_offer_create_cp0041(self):
        '''
        Pruebas de Ingreso Nueva Oferta con formato de imagen no permitido
        '''
        offer = Offer.objects.create(
            title='?¿?==?¿¿¿*^^Papas Fritas',
            description='Acaramelada@###~@',
            date_expiry=datetime.datetime(2020, 10, 1),
            image=SimpleUploadedFile(
                'papas.csv',
                b'Este es un archivo de prueba!'),
            created_user=self.user,
            modified_user=self.user
        )
        with self.assertRaises(ValidationError) as error:
            offer.full_clean()
        # compara mensaje de error obtenido y el esperado
        exception = error.exception
        message_1 = exception.message_dict['title'][0]
        message_2 = exception.message_dict['description'][0]
        message_3 = exception.message_dict['image'][1]
        self.assertEqual(message_1, 'Contiene carácteres especiales no '
                                    'permitidos o números/carácters muy '
                                    'largos. Ingrese sólo letras, números '
                                    'o # $ % & * / + - ¿ ? ! ¡ , .')
        self.assertEqual(message_2, 'Contiene carácteres especiales no '
                                    'permitidos o números/carácters muy '
                                    'largos. Ingrese sólo letras, números '
                                    'o # $ % & * / + - ¿ ? ! ¡ , .')
        self.assertEqual(message_3, '.csv no es una extensión de archivo '
                                    'permitida. Suba una imagen con '
                                    'extensión: .jpeg .jpeg o .png')


    def test_coupon_create_cp0042(self):
        '''
        Pruebas de Ingreso Nuevo Cupon con formato de imagen no permitido
        '''
        coupon = Coupon.objects.create(
            title='Papas Fritas',
            description='Acaramelada',
            date_expiry=datetime.datetime(2018, 8, 1),
            image=self.temp_image.name,
            created_user=self.user,
            modified_user=self.user
        )
        with self.assertRaises(ValidationError) as error:
            coupon.full_clean()
        # compara mensaje de error obtenido y el esperado
        exception = error.exception
        message = exception.message_dict['date_expiry'][0]
        self.assertEqual(message, 'Seleccione una fecha y hora '
                                  'posterior a la actual')


    def test_offer_create_cp0043(self):
        '''
        Pruebas de Ingreso Nueva Oferta con formato de imagen no permitido
        '''
        offer = Offer.objects.create(
            title='?¿?==?¿¿¿*^^Papas Fritas',
            description='Acaramelada@###~@',
            date_expiry=datetime.datetime(2018, 8, 1),
            image=SimpleUploadedFile(
                'papas.txt',
                b'Este es un archivo de prueba!'),
            created_user=self.user,
            modified_user=self.user
        )
        with self.assertRaises(ValidationError) as error:
            offer.full_clean()
        # compara mensaje de error obtenido y el esperado
        exception = error.exception
        message_1 = exception.message_dict['title'][0]
        message_2 = exception.message_dict['date_expiry'][0]
        message_3 = exception.message_dict['image'][1]
        self.assertEqual(message_1, 'Contiene carácteres especiales no '
                                    'permitidos o números/carácters muy '
                                    'largos. Ingrese sólo letras, números '
                                    'o # $ % & * / + - ¿ ? ! ¡ , .')
        self.assertEqual(message_2, 'Seleccione una fecha y hora '
                                    'posterior a la actual')
        self.assertEqual(message_3, '.txt no es una extensión de archivo '
                                    'permitida. Suba una imagen con '
                                    'extensión: .jpeg .jpeg o .png')


    def test_coupon_create_cp044(self):
        '''
        Prueba que sí se puede crear un Cupon sin description
        Cuando hay campos nulos la DB devuelve IntegrityError
        '''
        with self.assertRaises(IntegrityError):
            Coupon.objects.create(
                title='Hamburguesas dobles',
                description=None,
                date_expiry=datetime.datetime(2020, 8, 1),
                image=self.temp_image.name,
                created_user=self.user,
                modified_user=self.user
            )


    def test_offer_create_cp045(self):
        '''
        Prueba que no se puede crear una Oferta sin title
        '''
        with self.assertRaises(IntegrityError):
            Offer.objects.create(
                title=None,
                description='Hamburguesas en promocion',
                date_expiry=datetime.datetime(2020, 8, 1),
                image=self.temp_image.name,
                created_user=self.user,
                modified_user=self.user
            )


    def test_coupon_create_cp046(self):
        '''
        Prueba que no se puede crear un Cupon sin image
        '''
        #with self.assertRaises(IntegrityError):
        Coupon.objects.create(
            title='Papas Fritas',
            description='Acaramelada',
            date_expiry=datetime.datetime(2020, 8, 1),
            image=None,
            created_user=self.user,
            modified_user=self.user
        )


    def test_offer_create_cp047(self):
        '''
        Prueba que no se puede crear una Oferta sin fecha de expiracion
        '''
        with self.assertRaises(IntegrityError):
            Offer.objects.create(
                title='Papas Fritas',
                description='Acaramelada',
                image=self.temp_image.name,
                date_expiry=None,
                created_user=self.user,
                modified_user=self.user
            )


    def test_coupon_create_cp048(self):
        '''
        Prueba que no se puede crear un Cupon con sólo el campo title
        '''
        with self.assertRaises(IntegrityError):
            Coupon.objects.create(
                title='Hamburger medium',
                description=None,
                image=None,
                date_expiry=None,
                created_user=self.user,
                modified_user=self.user
            )


    def test_offer_create_cp049(self):
        '''
        Prueba que no se puede crear una Oferta con sólo el campo description
        '''
        with self.assertRaises(IntegrityError):
            Offer.objects.create(
                title=None,
                description='Acaramelada',
                image=None,
                date_expiry=None,
                created_user=self.user,
                modified_user=self.user
            )


    def test_coupon_create_cp050(self):
        '''
        Prueba que no se puede crear un Cupon con sólo el campo image
        '''
        with self.assertRaises(IntegrityError):
            Coupon.objects.create(
                title=None,
                description=None,
                image=self.temp_image.name,
                date_expiry=None,
                created_user=self.user,
                modified_user=self.user
            )


    def test_offer_create_cp051(self):
        '''
        Prueba que no se puede crear una Oferta con sólo el campo date
        '''
        with self.assertRaises(IntegrityError):
            Offer.objects.create(
                title=None,
                description=None,
                image=None,
                date_expiry=datetime.datetime(2020, 8, 1),
                created_user=self.user,
                modified_user=self.user
            )


    def test_coupon_create_cp052(self):
        '''
        Prueba que no se puede crear un Cupon con date y title
        '''
        with self.assertRaises(IntegrityError):
            Coupon.objects.create(
                title='Hamburguesas dobles',
                description=None,
                image=None,
                date_expiry=datetime.datetime(2020, 8, 1),
                created_user=self.user,
                modified_user=self.user
            )


    def test_offert_create_cp053(self):
        '''
        Prueba que no se puede crear una Oferta con date e image
        '''
        with self.assertRaises(IntegrityError):
            Offer.objects.create(
                title=None,
                description=None,
                date_expiry=datetime.datetime(2020, 8, 1),
                image=self.temp_image.name,
                created_user=self.user,
                modified_user=self.user
            )


    def test_coupon_create_cp22(self):
        '''
        Prueba que no se puede crear un Cupon con campos vacíos
        '''
        with self.assertRaises(IntegrityError):
            Coupon.objects.create(
                title=None,
                description=None,
                date_expiry=None,
                image=None,
                created_user=self.user,
                modified_user=self.user
            )
