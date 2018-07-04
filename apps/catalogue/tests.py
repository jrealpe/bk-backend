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
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model
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

    def get_image(self, temp_image):
        '''
        Retorna el nombre de una imagen cuadrada y roja que es guardada
        '''
        size = (200, 200)
        color = (255, 0, 0)
        image = Image.new('RGBA', size, color)
        image.save(temp_image, 'png')
        return temp_image

    def test_category_create_cp(self):
        '''
        Pruebas de Ingreso Nueva Categoria exitoso
        '''
        category = Category()
        category.name = 'category'
        temp_image = tempfile.NamedTemporaryFile()
        image = self.get_image(temp_image)
        category.image = image.name
        category.created_user = self.user
        category.modified_user = self.user
        category.save()
        self.assertEqual(len(Category.objects.all()), 1)
        return category

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_product_create_cp001(self):
        '''
        Pruebas de Ingreso Nuevo Producto exitoso
        El decorador sobrescribe la ruta de MEDIA_ROOT
        por la del directorio de archivos temporales del sistema
        '''
        product = Product()
        product.title = 'Papas Fritas'
        product.description = 'Acaramelada'
        product.category = self.test_category_create_cp()
        # crea un archivo temporal
        # con un nombre visible en el sistema de archivos
        temp_image = tempfile.NamedTemporaryFile()
        image = self.get_image(temp_image)
        product.image = image.name
        product.created_user = self.user
        product.modified_user = self.user
        product.save()
        print('It Worked!', product.image)
        self.assertEqual(len(Product.objects.all()), 1)


    def test_product_create_cp053(self):
        '''
        Prueba que no se puede crear un Product con sólo el campo title
        '''
        product = Product()
        product.title = 'Hamburguesa'
        with self.assertRaises(IntegrityError):
            product.save()
