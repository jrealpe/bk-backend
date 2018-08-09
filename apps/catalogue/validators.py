'''
Validaciones del sistema
'''
import datetime
import re
import os
from os.path import splitext
from django.core.exceptions import ValidationError


def date_validator(value):
    '''
    Validador de que las fechas sean mayor a la actual
    '''
    today = datetime.datetime.today()
    if value < today:
        raise ValidationError('Seleccione una fecha y hora posterior '
                              'a la actual')

def title_validator(value):
    '''
    Validar que como títulos ingresen sólo texto
    '''
    regex = re.compile('^[a-zA-Z ]+$')
    if not regex.match(value):
        raise ValidationError('Contiene números o carácteres especiales. ' \
                              + 'Ingrese sólo letras')


def description_validator(value):
    '''
    Validar que como descrición ingresen sólo letras y números
    '''
    regex = re.compile('^([A-ZÁÉÍÓÚa-záéíóú ]+[0-9#\$%&\*\/\+\-\,\.]{,10})+$')
    if not regex.match(value):
        raise ValidationError('Contiene carácteres especiales no permitidos' \
                              + ' o números/carácters muy largos. '
                              + 'Ingrese sólo letras, números o ' \
                              + '# $ % & * / + - , .')


def image_validator(value):
    '''
    Validar que la imagen sólo acepte jpg jpeg png como formatos de imagen
    '''
    allowed_extesions = ('.jpg', '.jpeg', '.png')
    ext = os.path.splitext(value.name)[1].lower()
    if not ext in allowed_extesions:
        raise ValidationError( ext + 
                              ' no es una extensión de archivo permitida. '
                              'Suba una imagen con extensión: '
                              '.jpeg .jpeg o .png')
