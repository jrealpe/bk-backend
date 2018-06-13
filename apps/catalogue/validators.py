''' 
Validaciones del sistema
'''
import datetime

from django.core.exceptions import ValidationError


def date_validator(value):
    '''
    Validador de que las fechas sean mayor a la actual
    '''
    today = datetime.datetime.today()
    if value < today:
        raise ValidationError('Seleccione una fecha y hora posterior '
                              'a la actual')
