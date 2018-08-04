'''
Those are models of the application
'''
from datetime import datetime
from django.db import models

from django.core.validators import MaxLengthValidator
from core.models import BaseModel
from .validators import date_validator, image_validator
from .validators import title_validator, description_validator


class Category(BaseModel):
    '''Category for each Product'''
    name = models.CharField(max_length=30, validators=[title_validator], unique = True)
    image = models.ImageField('Imagen',
                              upload_to='categories',
                              null=False,
                              validators=[image_validator])

    class Meta:
        '''Metadata for categories'''
        ordering = ['name']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Product(BaseModel):
    '''Prodcuts'''
    title = models.CharField('Titulo',
                             max_length=30,
                             validators=[title_validator])
    description = models.TextField('Descripcion',
                                   max_length=150,
                                   validators=[
                                       description_validator,
                                       MaxLengthValidator(150)
                                   ])
    category = models.ForeignKey(
        'Category',
        verbose_name='Categoria',
        on_delete=models.PROTECT,
    )
    image = models.ImageField('Imagen',
                              upload_to='products',
                              null=False,
                              validators=[image_validator])

    class Meta:
        '''Metadata for Product'''
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.title


class Promotion(BaseModel):
    '''Abstract Class
    Model of any type of promotion: Coupon or Offter
    '''
    title = models.CharField('Titulo',
                             max_length=30,
                             validators=[title_validator])
    description = models.TextField('Descripcion', blank=True, max_length=60)
    date_expiry = models.DateTimeField('Fecha de Expiracion',
                                       validators=[date_validator])
    image = models.ImageField('Imagen',
                              null=False,
                              validators=[image_validator])

    class Meta:
        ''''Defined class as abstract'''
        abstract = True

    def __str__(self):
        return self.title

    @property
    def is_past_due(self):
        '''Return true when date is past due'''
        return datetime.now() < self.date_expiry


class Coupon(Promotion):
    '''Promotion to 25 percent discount on products'''

    class Meta:
        '''Metadata for Coupon'''
        verbose_name = 'Cupon'
        verbose_name_plural = 'Cupones'


class Offer(Promotion):
    '''Promotion of combos and 2x1'''
    class Meta:
        '''Metadata for Offer'''
        verbose_name = 'Oferta'
        verbose_name_plural = 'Ofertas'
