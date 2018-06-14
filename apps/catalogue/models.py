'''
Those are models of the application
'''
from datetime import datetime
from django.db import models

from django.core.validators import RegexValidator
from core.models import BaseModel
from .validators import date_validator



class Category(BaseModel):
    '''Category for each Product'''
    name = models.CharField(max_length=30,
                            validators=[
                                RegexValidator(
                                    '[a-zA-Z\r]',
                                    'Ingrese solo letras',
                                    'No valido'
                                )
                            ])
    image = models.ImageField('Imagen', upload_to='categories')

    class Meta:
        '''Metadata for categories'''
        ordering = ['name']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Product(BaseModel):
    '''Prodcuts'''
    title = models.CharField('Titulo', max_length=30,
                             validators=[
                                 RegexValidator(
                                     '[a-zA-Z\r]',
                                     'Ingrese solo letras',
                                     'No valido'
                                 )
                             ])
    description = models.TextField('Descripcion', blank=True, max_length=150,
                                   validators=[
                                       RegexValidator(
                                           "([A-Za-z\r])\\w+",
                                           'Ingrese solo letras y números',
                                           'No valido'
                                       )
                                   ])
    category = models.ForeignKey(
        'Category',
        verbose_name='Categoria',
        on_delete=models.PROTECT,
    )
    image = models.ImageField('Imagen', upload_to='products')

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
    title = models.CharField('Titulo', max_length=30,
                             validators=[
                                 RegexValidator(
                                     '[a-zA-Z\r]',
                                     'Ingrese solo letras',
                                     'No valido'
                                 )
                             ])
    description = models.TextField('Descripcion', blank=True, max_length=60)
    date_expiry = models.DateTimeField('Fecha de Expiracion',
                                       validators=[date_validator])
    image = models.ImageField('Imagen')

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
