from django.db import models
from django.utils import timezone

from core.models import BaseModel

from .validators import date_validator


class Category(BaseModel):
    name = models.CharField('Nombre', max_length=30)

    class Meta:
        ordering = ['name']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.name 


class Product(BaseModel):
    title = models.CharField('Titulo', max_length=30)
    description = models.TextField('Descripcion', max_length=50)
    category = models.ForeignKey(
        'Category',
        verbose_name='Categoria',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    image = models.ImageField('Imagen', upload_to='products')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.title


class Coupon(BaseModel):
    title = models.CharField('Titulo', max_length=30)
    description = models.TextField('Descripcion', blank=True, max_length=50)
    image = models.ImageField('Imagen', upload_to='coupons')
    date_expiry = models.DateTimeField('Fecha de Expiracion',
        validators=[date_validator])

    class Meta:
        verbose_name = 'Cupon'
        verbose_name_plural = 'Cupones'

    def __str__(self):
        return self.title
