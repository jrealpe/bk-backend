'''
Those are models pf the application
'''
from datetime import datetime, timedelta
from django.db import models
from core.models import BaseModel

from .validators import date_validator

def timestap():
    '''Return a timestap for the expiry dates'''
    now = datetime.now()
    start = now.replace(hour=18, minute=0, second=0, microsecond=0)
    return start + timedelta(days=1)


class Category(BaseModel):
    '''Category for each Product'''
    name = models.CharField('Nombre', max_length=30)

    class Meta:
        '''Metadata for categories'''
        ordering = ['name']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Product(BaseModel):
    '''Prodcuts'''
    title = models.CharField('Titulo', max_length=30)
    description = models.TextField('Descripcion', max_length=100)
    category = models.ForeignKey(
        'Category',
        verbose_name='Categoria',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    image = models.ImageField('Imagen', upload_to='products')

    class Meta:
        '''Metadata for Product'''
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.title


class Coupon(BaseModel):
    '''Promotion to 25 percent discount on products'''
    title = models.CharField('Titulo', max_length=30)
    description = models.TextField('Descripcion', blank=True, max_length=100)
    image = models.ImageField('Imagen', upload_to='coupons')
    date_expiry = models.DateTimeField('Fecha de Expiracion', default=timestap,
                                       validators=[date_validator])

    class Meta:
        '''Metadata for Coupon'''
        verbose_name = 'Cupon'
        verbose_name_plural = 'Cupones'

    def __str__(self):
        return self.title

    @property
    def is_past_due(self):
        '''Return true when date is past due'''
        return datetime.now > self.date_expiry

class Offer(BaseModel):
    '''Promotion of combos and 2x1'''
    title = models.CharField('Titulo', max_length=30)
    description = models.TextField('Descripcion', blank=True, max_length=100)
    image = models.ImageField('Imagen', upload_to='offers')
    date_expiry = models.DateTimeField('Fecha de Expiracion', default=timestap,
                                       validators=[date_validator])

    class Meta:
        '''Metadata for Offer'''
        verbose_name = 'Oferta'
        verbose_name_plural = 'Ofertas'

    def __str__(self):
        return self.title

    @property
    def is_past_due(self):
        '''Return true when date is past due'''
        return datetime.now > self.date_expiry
