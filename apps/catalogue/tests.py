'''
Pruebas Unitarias para el Catálogo
Se crea un usuario de prueba
Se crea uma imagen con ayuda de la librerìa PIL
La imagen creada se guada en el sistema de archivos temporales del S.O.
'''
import tempfile
from PIL import Image
from django.test import TestCase
from django.test import override_settings
from django.db.utils import IntegrityError, DataError
from django.db import models
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Product, Category

USER = get_user_model()

class TestProduct(TestCase):
    '''
    Pruebas unitarias para Productos del catálogo
	'''

    def setUp(self):
        '''
        Crea un usuario y contraseña para todas las pruebas que lo necesiten
        '''
        self.user = USER.objects.create_user(
            username='admin',
            password='@dm1n112233'
        )

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def get_image(self):
        '''
        Retorna la ruta de una imagen cuadrada y roja que es guardada
        El decorador sobrescribe la ruta de MEDIA_ROOT
        por la del directorio de archivos temporales del sistema
        '''
        size = (200, 200)
        color = (255, 0, 0)
        image = Image.new('RGB', size, color)
        # crea un archivo temporal
        # con un nombre visible en el sistema de archivos
        temp_image = tempfile.NamedTemporaryFile()
        image.save(temp_image, 'png')
        return temp_image.name


    def test_category_create_cp(self):
        '''
        Pruebas de Ingreso Nueva Categoria exitoso
        '''
        category = Category()
        category.name = 'Dobles'
        category.image = self.get_image()
        category.created_user = self.user
        category.modified_user = self.user
        category.save()
        return category


    def test_product_create_cp001(self):
        '''
        Pruebas de Ingreso Nuevo Producto exitoso
        '''
        product = Product.objects.create(
            title = 'Papas Fritas',
            description = 'Acaramelada',
            category = self.test_category_create_cp(),
            image = self.get_image(),
            created_user = self.user,
            modified_user = self.user
        )
        print('It Worked!', product.image)
        self.assertEqual(len(Product.objects.all()), 1)
        # no es la forma correcta para verificar que se ha crado
        # Product.objects.get(title='Papas Fritas') retorna 'Papas Fritas'


    def test_product_create_cp002(self):
        '''
        Pruebas de Ingreso Nuevo Producto con título mayor a 30 caracteres
        '''
        with self.assertRaises(DataError):
            product = Product.objects.create(
                title = 'Papas Fritas y algo más de 30 caracteres',
                description = 'Acaramelada',
                category = self.test_category_create_cp(),
                image = self.get_image(),
                created_user = self.user,
                modified_user = self.user
            )


    def test_product_create_cp003(self):
        '''
        Pruebas de Ingreso Nuevo Producto con título de números
        '''
        product = Product.objects.create(
            title = '1112253652Papas Fritas',
            description = 'Acaramelada',
            category = self.test_category_create_cp(),
            image = self.get_image(),
            created_user = self.user,
            modified_user = self.user
        )
        self.assertNotRegex(product.title, r'^[a-zA-Z ]+$')
        # falta verificar error, que no se guardó el producto


    def test_product_create_cp004(self):
        '''
        Pruebas de Ingreso Nuevo Producto con título más 30 caracteres números
        '''
        with self.assertRaises(DataError):
            product = Product.objects.create(
                title = '1112253652Papas Fritas' \
                + 'y algo más de 30 caracteres',
                description = 'Acaramelada',
                category = self.test_category_create_cp(),
                image = self.get_image(),
                created_user = self.user,
                modified_user = self.user
            )
            self.assertNotRegex(product.title, r'^[a-zA-Z ]+$')


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
            category = self.test_category_create_cp(),
            image = self.get_image(),
            created_user = self.user,
            modified_user = self.user
        )
        product.save() # No acepta que hay DataError como en titulo


    def test_product_create_cp006(self):
        '''
        Pruebas de Ingreso Nuevo Producto con descripción no alfanumérica
        '''
        product = Product.objects.create(
            title = 'Papas Fritas',
            description = 'Acaramelada@###~@',
            category = self.test_category_create_cp(),
            image = self.get_image(),
            created_user = self.user,
            modified_user = self.user
        )
        self.assertNotRegex(product.description, r'^[A-Za-z0-9 ]+$')
        # falta verificar error, que no se guardó el producto


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
            category = self.test_category_create_cp(),
            image = self.get_image(),
            created_user = self.user,
            modified_user = self.user
        )
        self.assertNotRegex(product.description, r'^[A-Za-z0-9 ]+$')
        # falta verificar error, que no se guardó el producto


    def test_product_create_cp008(self):
        '''
        Pruebas de Ingreso Nuevo Producto exitoso
        '''
        product = Product.objects.create(
            title = 'Papas Fritas',
            description = 'Acaramelada',
            category = self.test_category_create_cp(),
            image = SimpleUploadedFile(
                'file.txt',
                b'Este es un archivo de prueba!'),
            created_user = self.user,
            modified_user = self.user
        )
        # falta verificar error, que no se guardó el producto


    def test_product_create_cp024(self):
        '''
        Prueba que no se puede crear un Product sin description
        '''
        with self.assertRaises(IntegrityError):
            product = Product.objects.create(
                title='Hamburguesas dobles',
                description = None,
                category=self.test_category_create_cp(),
                image=self.get_image(),
                created_user=self.user,
                modified_user=self.user
            )


    def test_product_create_cp025(self):
        '''
        Prueba que no se puede crear un Product sin title
        '''
        with self.assertRaises(IntegrityError):
            product = Product.objects.create(
                title = None,
                description = 'Hamburguesas en promocion',
                category = self.test_category_create_cp(),
                image = self.get_image(),
                created_user = self.user,
                modified_user = self.user
            )


    def test_product_create_cp026(self):
        '''
        Prueba que no se puede crear un Product sin image
        '''
        with self.assertRaises(IntegrityError):
            product = Product.objects.create(
                title = 'Papas Fritas',
                description = 'Acaramelada',
                category = self.test_category_create_cp(),
                image = None,
                created_user = self.user,
                modified_user = self.user
           )


    def test_product_create_cp027(self):
        '''
        Prueba que no se puede crear un Product sin category
        '''
        with self.assertRaises(IntegrityError):
            product = Product.objects.create(
                title = 'Papas Fritas',
                description = 'Acaramelada',
                image = self.get_image(),
                category = None,
                created_user = self.user,
                modified_user = self.user
            )


    def test_product_create_cp028(self):
        '''
        Prueba que no se puede crear un Product sin description ni category
        '''
        with self.assertRaises(IntegrityError):
            product = Product.objects.create(
                title = 'Papas Fritas',
                description = None,
                category = None,
                image = self.get_image(),
                created_user = self.user,
                modified_user = self.user
            )


    def test_product_create_cp029(self):
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


    def test_product_create_cp030(self):
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


    def test_product_create_cp031(self):
        '''
        Prueba que no se puede crear un Product con sólo el campo image
        '''
        with self.assertRaises(IntegrityError):
            product = Product.objects.create(
                title = None,
                description = None,
                image = self.get_image(),
                category = None,
                created_user = self.user,
                modified_user = self.user
            )


    def test_product_create_cp032(self):
        '''
        Prueba que no se puede crear un Product con sólo el campo category
        '''
        with self.assertRaises(IntegrityError):
            product = Product.objects.create(
                title = None,
                description = None,
                image = None, 
                category = self.test_category_create_cp(),
                created_user = self.user,
                modified_user = self.user
            )


    def test_product_create_cp033(self):
        '''
        Prueba que no se puede crear un Product con category y title
        '''
        with self.assertRaises(IntegrityError):
            Product.objects.create(
                title = 'Hamburguesas dobles',
                description = None,
                image = None,
                category = self.test_category_create_cp(),
                created_user = self.user,
                modified_user = self.user
            )


    def test_product_create_cp034(self):
        '''
        Prueba que no se puede crear un Product con category e image
        '''
        with self.assertRaises(IntegrityError):
            Product.objects.create(
                title = None,
                description = None,
                category = self.test_category_create_cp(),
                image = self.get_image(),
                created_user = self.user,
                modified_user = self.user
            )


    def test_product_create_cp35(self):
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
