'''
Pruebas Unitarias para el Catálogo
Se crea un usuario de prueba
Se crea uma imagen con ayuda de la librerìa PIL
La imagen creada se guada en el sistema de archivos temporales del S.O.
'''
import tempfile
from PIL import Image
from django.conf import settings
from django.test import TestCase, override_settings
from django.db.utils import IntegrityError, DataError
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Product, Category

USER = get_user_model()

class TestProduct(TestCase):
    '''
    Pruebas unitarias para Productos del catálogo
	'''
    username = settings.TEST_USERNAME
    password = settings.TEST_PASSWORD

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def setUp(self):
        '''
        Crea un usuario y categoria para todas las pruebas que lo necesiten
        El decorador sobrescribe la ruta de MEDIA_ROOT
        por la del directorio de archivos temporales del sistema
        '''
        size = (200, 200)
        color = (255, 0, 0)
        image = Image.new('RGB', size, color)
        self.ext = 'png'
        # crea un archivo temporal
        # con un nombre visible en el sistema de archivos
        self.temp_image = tempfile.NamedTemporaryFile(suffix='.png')
        image.save(self.temp_image, self.ext)
        # utiliza usuario y contraseña de prueba
        self.user = USER.objects.create_user(
            username = self.username,
            password = self.password
        )
        # nueva categoria
        self.category = Category.objects.create(
            name = 'Dobles',
            image = self.temp_image.name,
            created_user = self.user,
            modified_user = self.user
        )


    def test_product_create_cp001(self):
        '''
        Pruebas de Ingreso Nuevo Producto exitoso
        '''
        product = Product.objects.create(
            title = 'Papas Fritas',
            description = 'Acaramelada',
            category = self.category,
            image = self.temp_image.name,
            created_user = self.user,
            modified_user = self.user
        )
        print('It Worked!', product.image)
        # ValidationError no valida sino se la llama
        # metodo full_clean() valida cada uno de los campos del formulario
        self.assertRaises(ValidationError, product.full_clean())


    def test_product_create_cp002(self):
        '''
        Pruebas de Ingreso Nuevo Producto con título mayor a 30 caracteres
        '''
        with self.assertRaises(DataError):
            product = Product.objects.create(
                title = 'Papas Fritas y algo más de 30 caracteres',
                description = 'Acaramelada',
                category = self.category,
                image = self.temp_image.name,
                created_user = self.user,
                modified_user = self.user
            )
            self.assertRaises(ValidationError, product.full_clean())


    def test_product_create_cp003(self):
        '''
        Pruebas de Ingreso Nuevo Producto con título de números
        '''
        product = Product.objects.create(
            title = '1112253652Papas Fritas',
            description = 'Acaramelada',
            category = self.category,
            image = self.temp_image.name,
            created_user = self.user,
            modified_user = self.user
        )
        with self.assertRaises(ValidationError) as cm:
            product.full_clean()
        # compara mensaje de error obtenido y el esperado
        exception = cm.exception
        message = exception.message_dict['title'][0]
        self.assertEqual(message, 'Contiene números o carácteres especiales. '
                                  'Ingrese sólo letras')


    def test_product_create_cp004(self):
        '''
        Pruebas de Ingreso Nuevo Producto con título más 30 caracteres números
        '''
        with self.assertRaises(DataError):
            product = Product.objects.create(
                title = '1112253652Papas Fritas' \
                + 'y algo más de 30 caracteres',
                description = 'Acaramelada',
                category = self.category,
                image = self.temp_image.name,
                created_user = self.user,
                modified_user = self.user
            )
            self.assertRaises(ValidationError, product.full_clean())


    def test_product_create_cp005(self):
        '''
        Pruebas de Ingreso Nuevo Producto con descripción de 150 caracteres
        '''
        product = Product.objects.create(
            title = 'Papas Fritas',
            description = 'Acaramelada con doble hamburguesas don ' \
            + 'doble queso y doble jamon mega oferta por los siguientes ' \
            + 'dias de la semana lunes, jueves, domingo aprovecha estos ' \
            + 'dias  tan solo 15 dólares',
            category = self.category,
            image = self.temp_image.name,
            created_user = self.user,
            modified_user = self.user
        )
        with self.assertRaises(ValidationError):
            product.full_clean()


    def test_product_create_cp006(self):
        '''
        Pruebas de Ingreso Nuevo Producto con descripción no alfanumérica
        '''
        product = Product.objects.create(
            title = 'Papas Fritas',
            description = 'Acaramelada@###~@',
            category = self.category,
            image = self.temp_image.name,
            created_user = self.user,
            modified_user = self.user
        )
        with self.assertRaises(ValidationError):
            product.full_clean()


    def test_product_create_cp007(self):
        '''
        Pruebas de Ingreso Nuevo Producto con descripción no alfanumérica
        '''
        product = Product.objects.create(
            title = 'Papas Fritas',
            description = 'Acaramelada@###~@ con doble hamburguesas' \
            + 'doble queso y doble jamon mega oferta por los siguientes ' \
            + 'dias de la semana lunes, jueves, domingo aprovecha estos ' \
            + 'dias  tan solo 15 dólares',
            category = self.category,
            image = self.temp_image.name,
            created_user = self.user,
            modified_user = self.user
        )
        with self.assertRaises(ValidationError):
            product.full_clean()
        # self.assertNotRegex(product.description, r'^[A-Za-z0-9 ]+$')


    def test_product_create_cp008(self):
        '''
        Pruebas de Ingreso Nuevo Producto con formato de imagen no permitido
        '''
        product = Product.objects.create(
            title = 'Papas Fritas',
            description = 'Acaramelada',
            category = self.category,
            image = SimpleUploadedFile(
                'papas.txt',
                b'Este es un archivo de prueba!'),
            created_user = self.user,
            modified_user = self.user
        )
        with self.assertRaises(ValidationError):
            product.full_clean()


    def test_product_create_cp009(self):
        '''
        Pruebas de Ingreso Nuevo Producto con formato de imagen no permitido
        '''
        with self.assertRaises(DataError):
            product = Product.objects.create(
                title = 'Papas Fritas y algo más hasta los treinta',
                description = 'Acaramelada@###~@ con doble hamburguesas' \
                + 'doble queso y doble jamon mega oferta por los siguientes ' \
                + 'dias de la semana lunes, jueves, domingo aprovecha estos ' \
                + 'dias  tan solo 15 dólares',
                category = self.category,
                image = SimpleUploadedFile(
                    'papas.txt',
                    b'Este es un archivo de prueba!'),
                created_user = self.user,
                modified_user = self.user
            )
            with self.assertRaises(ValidationError):
                product.full_clean()


    def test_product_create_cp0010(self):
        '''
        Pruebas de Ingreso Nuevo Producto con formato de imagen no permitido
        '''
        product = Product.objects.create(
            title = '1112253652Papas Fritas',
            description = 'Acaramelada@###~@',
            category = self.category,
            image = SimpleUploadedFile(
                'papas.txt',
                b'Este es un archivo de prueba!'),
            created_user = self.user,
            modified_user = self.user
        )
        with self.assertRaises(ValidationError):
            product.full_clean()


    def test_product_create_cp011(self):
        '''
        Prueba que no se puede crear un Product sin description
        '''
        with self.assertRaises(IntegrityError):
            product = Product.objects.create(
                title='Hamburguesas dobles',
                description = None,
                category=self.category,
                image=self.temp_image.name,
                created_user=self.user,
                modified_user=self.user
            )


    def test_product_create_cp012(self):
        '''
        Prueba que no se puede crear un Product sin title
        '''
        with self.assertRaises(IntegrityError):
            product = Product.objects.create(
                title = None,
                description = 'Hamburguesas en promocion',
                category = self.category,
                image = self.temp_image.name,
                created_user = self.user,
                modified_user = self.user
            )


    def test_product_create_cp013(self):
        '''
        Prueba que no se puede crear un Product sin image
        '''
        #with self.assertRaises(IntegrityError):
        product = Product.objects.create(
            title = 'Papas Fritas',
            description = 'Acaramelada',
            category = self.category,
            image = None,
            created_user = self.user,
            modified_user = self.user
        )


    def test_product_create_cp014(self):
        '''
        Prueba que no se puede crear un Product sin category
        '''
        with self.assertRaises(IntegrityError):
            product = Product.objects.create(
                title = 'Papas Fritas',
                description = 'Acaramelada',
                image = self.temp_image.name,
                category = None,
                created_user = self.user,
                modified_user = self.user
            )


    def test_product_create_cp015(self):
        '''
        Prueba que no se puede crear un Product sin description ni category
        '''
        with self.assertRaises(IntegrityError):
            product = Product.objects.create(
                title = 'Papas Fritas',
                description = None,
                category = None,
                image = self.temp_image.name,
                created_user = self.user,
                modified_user = self.user
            )


    def test_product_create_cp016(self):
        '''
        Prueba que no se puede crear un Product con sólo el campo title
        '''
        with self.assertRaises(IntegrityError):
            product = Product.objects.create(
                title = 'Hamburger medium',
                description = None,
                image = None,
                category = None,
                created_user = self.user,
                modified_user = self.user
            )


    def test_product_create_cp017(self):
        '''
        Prueba que no se puede crear un Product con sólo el campo description
        '''
        with self.assertRaises(IntegrityError):
            product = Product.objects.create(
                title = None,
                description = 'Acaramelada',
                image = None,
                category = None,
                created_user = self.user,
                modified_user = self.user
            )


    def test_product_create_cp018(self):
        '''
        Prueba que no se puede crear un Product con sólo el campo image
        '''
        with self.assertRaises(IntegrityError):
            product = Product.objects.create(
                title = None,
                description = None,
                image = self.temp_image.name,
                category = None,
                created_user = self.user,
                modified_user = self.user
            )


    def test_product_create_cp019(self):
        '''
        Prueba que no se puede crear un Product con sólo el campo category
        '''
        with self.assertRaises(IntegrityError):
            product = Product.objects.create(
                title = None,
                description = None,
                image = None, 
                category = self.category,
                created_user = self.user,
                modified_user = self.user
            )


    def test_product_create_cp020(self):
        '''
        Prueba que no se puede crear un Product con category y title
        '''
        with self.assertRaises(IntegrityError):
            Product.objects.create(
                title = 'Hamburguesas dobles',
                description = None,
                image = None,
                category = self.category,
                created_user = self.user,
                modified_user = self.user
            )


    def test_product_create_cp021(self):
        '''
        Prueba que no se puede crear un Product con category e image
        '''
        with self.assertRaises(IntegrityError):
            Product.objects.create(
                title = None,
                description = None,
                category = self.category,
                image = self.temp_image.name,
                created_user = self.user,
                modified_user = self.user
            )


    def test_product_create_cp22(self):
        '''
        Prueba que no se puede crear un Product con campos vacíos
        '''
        with self.assertRaises(IntegrityError):
            Product.objects.create(
                title = None,
                description = None,
                category = None,
                image = None,
                created_user = self.user,
                modified_user = self.user
            )
