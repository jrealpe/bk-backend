from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import BaseModel


########
# User #
########

class User(AbstractUser):
    identification = models.CharField('Identificación', max_length=13)
    phone = models.CharField('Teléfono de trabajo', max_length=10)
    province = models.ForeignKey(
        'address.Province',
        verbose_name='Provincia',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    city = models.ForeignKey(
        'address.City',
        verbose_name='Ciudad',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.username
