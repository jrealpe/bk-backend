from django.db import models
from datetime import date
import django.utils.timezone

from core.models import BaseModel


class Category(models.Model):
    name = models.CharField('Nombre', max_length=50)

    class Meta:
        ordering = ['name']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.name 


class Product(BaseModel):
    title = models.CharField('Titulo', max_length=60)
    description = models.TextField('Descripcion', max_length=150)
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
    title = models.CharField('Titulo', max_length=60)
    description = models.TextField('Descripcion', max_length=150, blank=True)
    image = models.ImageField('Imagen', upload_to='coupons')
    date_expiry = models.DateTimeField('Fecha de Expiracion')

    class Meta:
        verbose_name = 'Cupon'
        verbose_name_plural = 'Cupones'

    def __str__(self):
        return self.title

    @property
    def is_past_due(self):
        return date.today > self.date_expiry
