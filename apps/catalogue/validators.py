import datetime

from django.core.exceptions import ValidationError


def date_validator(value):
    today = datetime.datetime.today()
    if value < today:
        raise ValidationError('Seleccione una fecha y hora posterior '
                              'a la actual')
