from django.db import models

from core.models import BaseModel


class Product(BaseModel):
    title = models.CharField('Titulo', max_length=200)
    description = models.TextField('Descripcion')
    image = models.ImageField('Imagen', upload_to='products')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.title


class Coupon(models.Model):
    title = models.CharField('Titulo', max_length=200)
    description = models.TextField('Descripcion', blank=True)
    image = models.ImageField('Imagen', upload_to='coupons')

    class Meta:
        verbose_name = 'Cupon'
        verbose_name_plural = 'Cupones'

    def __str__(self):
        return self.title
