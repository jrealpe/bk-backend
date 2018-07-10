''' 
Validaciones del sistema
'''
import datetime
import re
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
    if !regex.match(value):
        raise ValidationError('%s debe contener sólo letras' % value)


def description_validator(value):
    '''
    Validar que como descrición ingresen sólo letras y números
    '''
    regex = re.compile('^[A-Za-z0-9 ]+$')
    if !regex.match(value):
        raise ValidationError('%s debe contener sólo letras y números' % value)


def image_validator(value):
    '''
    Validar que la imagen sólo acepte jpg jpeg png como formatos de imagen
    '''
    allowed_extesions = ('.jpg', '.jpeg', .'png')
    ext = splitext(value.name)[1][1:].lower()
    if not ext in allowed_extesions:
        raise ValidationError('Extensión %s no está permitido. ' \
                              + 'Suba una imagen con extensión: ' \
                              + '.jpeg .jpeg o .png ')
