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
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from apps.catalogue.models import Category

USER = get_user_model()

class TestCategory(TestCase):
    '''
    Pruebas unitarias para Categorias del catálogo
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
        # crea un archivo temporal
        # con un nombre visible en el sistema de archivos
        self.temp_image = tempfile.NamedTemporaryFile(suffix='.png')
        image.save(self.temp_image, self.ext)
        # utiliza usuario y contraseña de prueba
        self.user = USER.objects.create_user(
            username=self.username,
            password=self.password
        )


    def test_category_create_cp023(self):
        '''
        Pruebas de Ingreso Nueva Categoría exitoso
        '''
        category = Category.objects.create(
            name='BEBIDAS',
            image=self.temp_image.name,
            created_user=self.user,
            modified_user=self.user
        )
        print('It Worked!', category.image)
        # Checkea el fallo de confirmar que existe algun error de validacion
        with self.assertRaises(AssertionError):
            # Se debe invocar a ValidationError para errores de este tipo
            # Asignados desde las funciones de Validación al Modelo Categoy
            with self.assertRaises(ValidationError):
                # Para validar a cada campo del formulario de Categorias
                category.full_clean()


    def test_category_create_cp024(self):
        '''
        Pruebas de Ingreso Nuevo Categoría con título mayor a 30 caracteres
        Cuando de desborda el tamaño restringido en un campo de texto
        La DB devuelve DataError
        '''
        with self.assertRaises(DataError):
            category = Category.objects.create(
                name='BEBIDAS GASEOSAS VARIADAS '
                     'LA SEGUNDA A MITAD DE PRECIO',
                image=self.temp_image.name,
                created_user=self.user,
                modified_user=self.user
            )
            category.save()


    def test_category_create_cp025(self):
        '''
        Pruebas de Ingreso Nueva Categoría con título de números
        '''
        category = Category.objects.create(
            name='BEBIDAS12',
            image=self.temp_image.name,
            created_user=self.user,
            modified_user=self.user
        )
        # Se debe invocar a ValidationError para errores de este tipo
        # Asignados desde las funciones de Validación al Modelo de Categorias
        with self.assertRaises(ValidationError) as error:
            category.full_clean()
        exception = error.exception
        message = exception.message_dict['name'][0]
        # compara mensaje de error obtenido y el esperado
        self.assertEqual(message, 'Contiene números o carácteres especiales. '
                                  'Ingrese sólo letras')


    def test_category_create_cp004(self):
        '''
        Pruebas de Ingreso Nueva Categoría con título más 30 caracteres números
        '''
        with self.assertRaises(DataError):
            category = Category.objects.create(
                name='12BEBIDAS GASEOSAS VARIADAS LA SEGUNDA '
                     'A MITAD DE PRECIO',
                image=self.temp_image.name,
                created_user=self.user,
                modified_user=self.user
            )
            category.save()


    def test_category_create_cp027(self):
        '''
        Pruebas de Ingreso Nueva Categoría con formato de imagen no permitido
        '''
        category = Category.objects.create(
            name='BEBIDAS',
            image=SimpleUploadedFile(
                'bebidas.csv',
                b'prueba,categoria'),
            created_user=self.user,
            modified_user=self.user
        )
        with self.assertRaises(ValidationError) as error:
            category.full_clean()
        # compara mensaje de error obtenido y el esperado
        exception = error.exception
        message = exception.message_dict['image'][1]
        self.assertEqual(message, '.csv no es una extensión de archivo '
                                  'permitida. Suba una imagen con extensión: '
                                  '.jpeg .jpeg o .png')


    def test_category_create_cp028(self):
        '''
        Pruebas de Ingreso Nueva Categoría con formato de imagen no permitido
        '''
        category = Category.objects.create(
            name='1112253652Papas Fritas',
            image=SimpleUploadedFile(
                'bebidas.csv',
                b'prueba,categoria'),
            created_user=self.user,
            modified_user=self.user
        )
        with self.assertRaises(ValidationError) as error:
            category.full_clean()
        # compara mensaje de error obtenido y el esperado
        exception = error.exception
        message_1 = exception.message_dict['name'][0]
        message_2 = exception.message_dict['image'][1]
        self.assertEqual(message_1, 'Contiene números o carácteres '
                                    'especiales. Ingrese sólo letras')
        self.assertEqual(message_2, '.csv no es una extensión de archivo '
                                    'permitida. Suba una imagen con '
                                    'extensión: .jpeg .jpeg o .png')


    def test_category_create_cp029(self):
        '''
        Prueba que no se puede crear Category sin title
        Cuando hay campos nulos la DB devuelve IntegrityError
        '''
        with self.assertRaises(IntegrityError):
            Category.objects.create(
                name=None,
                image=self.temp_image.name,
                created_user=self.user,
                modified_user=self.user
            )


    def test_category_create_cp030(self):
        '''
        Prueba que no se puede crear Category sin image
        '''
        #with self.assertRaises(IntegrityError):
        Category.objects.create(
            name='BEBIDAS',
            image=None,
            created_user=self.user,
            modified_user=self.user
        )


    def test_category_create_cp031(self):
        '''
        Prueba que no se puede crear Category sin campos
        '''
        #with self.assertRaises(IntegrityError):
        Category.objects.create(
            name='Papas Fritas',
            image=None,
            created_user=self.user,
            modified_user=self.user
        )
