from django.db import models
from django.conf import settings


class BaseModel(models.Model):
    created_at = models.DateTimeField('Fecha de creación', auto_now_add=True)
    modified_at = models.DateTimeField('Fecha de modificación', auto_now=True)
    created_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Creado por',
        on_delete=models.PROTECT,
        related_name='+'
    )
    modified_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Modificado por',
        on_delete=models.PROTECT,
        related_name='+'
    )
    is_active = models.BooleanField('¿Está activo?', default=True)

    class Meta:
        abstract = True
