from django.db import models


class Province(models.Model):
    iso_3166_2 = models.CharField(
        'ISO 3166-2', 
        max_length=3, 
        blank=True
    )
    name = models.CharField('Nombre', max_length=30)

    class Meta:
        ordering = ['name']
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'

    @property
    def code(self):
        return self.iso_3166_2

    def __str__(self):
        return self.name


class City(models.Model):
    province = models.ForeignKey(
        'address.Province',
        on_delete=models.PROTECT,
        verbose_name='Provincia'
    )
    name = models.CharField('Nombre', max_length=40)

    class Meta:
        ordering = ['name']
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

    def __str__(self):
        return self.name
