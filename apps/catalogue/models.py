from django.db import models
import django.utils.timezone

from core.models import BaseModel


class Category(models.Model):
    name = models.CharField('Nombre', max_length=200)

    class Meta:
        ordering = ['name']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.name 


class Product(BaseModel):
    title = models.CharField('Titulo', max_length=200)
    description = models.TextField('Descripcion')
    category = models.ForeignKey(
        'Category',
        verbose_name='Categoria',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    image = models.ImageField('Imagen', upload_to='products')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False,
        verbose_name='Actuaizado',
        blank=True,
        null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True,
        verbose_name='Publicado',
        blank=True,
        null=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.title


class Coupon(models.Model):
    title = models.CharField('Titulo', max_length=200)
    description = models.TextField('Descripcion', blank=True)
    image = models.ImageField('Imagen', upload_to='coupons')
    valid_until = models.DateTimeField(
        default=django.utils.timezone.now,
        blank=True,
        verbose_name='Fecha de fin de Vigencia')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False,
        verbose_name='Actuaizado',
        blank=True,
        null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True,
        verbose_name='Publicado',
        blank=True,
        null=True)

    class Meta:
        verbose_name = 'Cupon'
        verbose_name_plural = 'Cupones'

    def __str__(self):
        return self.title

