from django.db import models


class UserRecord(models.Model):
    """
    A record of a user's activity.
    """

    user = models.OneToOneField('customer.User', verbose_name='Usuario',
                                on_delete=models.CASCADE)

    # Browsing stats
    num_product_views = models.PositiveIntegerField(
        'Vistas de Producto', default=0)
    num_coupon_views = models.PositiveIntegerField(
        'Vistas de Cupones', default=0)
    num_offer_views = models.PositiveIntegerField(
        'Vistas de Ofertas', default=0)

    class Meta:
        verbose_name = 'Historial de Usuario'
        verbose_name_plural = 'Historial de Usuarios'


class ProductRecord(models.Model):
    """
    A record of a how popular a product is.
    This used be auto-merchandising to display the most popular
    products.
    """

    product = models.OneToOneField(
        'catalogue.Product', verbose_name='Producto',
        related_name='stats', on_delete=models.PROTECT)

    # Data used for generating a score
    num_views = models.PositiveIntegerField('Visualizaciones', default=0)

    class Meta:
        ordering = ['-num_views']
        verbose_name = 'Historial de Producto'
        verbose_name_plural = 'Historial de Productos'

    def __str__(self):
        return 'Registro para \'%s\'' % self.product


class UserProductView(models.Model):

    user = models.ForeignKey(
        'customer.User', verbose_name='Usuario',
        on_delete=models.CASCADE)
    product = models.ForeignKey(
        'catalogue.Product',
        on_delete=models.CASCADE,
        verbose_name='Producto')
    date_created = models.DateTimeField('Fecha de Creación', auto_now_add=True)

    class Meta:
        verbose_name = 'Visualización de Usuario-Producto'
        verbose_name_plural = 'Visualizaciones de Usuario-Producto'

    def __str__(self):
        return "%(user)s vió '%(product)s'" % {
            'user': self.user, 'product': self.product}


class CouponRecord(models.Model):
    """
    A record of a how popular a coupon is.
    This used be auto-merchandising to display the most popular
    coupon.
    """

    coupon = models.OneToOneField(
        'catalogue.Coupon', verbose_name='Cupón',
        related_name='stats', on_delete=models.PROTECT)

    # Data used for generating a score
    num_views = models.PositiveIntegerField('Visualizaciones', default=0)

    class Meta:
        ordering = ['-num_views']
        verbose_name = 'Historial de Cupón'
        verbose_name_plural = 'Historial de Cupones'

    def __str__(self):
        return 'Registro para \'%s\'' % self.product


class UserCouponView(models.Model):

    user = models.ForeignKey(
        'customer.User', verbose_name='Usuario',
        on_delete=models.CASCADE)
    coupon = models.ForeignKey(
        'catalogue.Coupon',
        on_delete=models.CASCADE,
        verbose_name='Cupón')
    date_created = models.DateTimeField('Fecha de Creación', auto_now_add=True)

    class Meta:
        verbose_name = 'Visualización de Usuario-Cupón'
        verbose_name_plural = 'Visualizaciones de Usuario-Cupón'

    def __str__(self):
        return "%(user)s vió '%(coupon)s'" % {
            'user': self.user, 'coupon': self.coupon}


class OfferRecord(models.Model):
    """
    A record of a how popular a offer is.
    This used be auto-merchandising to display the most popular
    offer.
    """

    offer = models.OneToOneField(
        'catalogue.Offer', verbose_name='Oferta',
        related_name='stats', on_delete=models.PROTECT)

    # Data used for generating a score
    num_views = models.PositiveIntegerField('Visualizaciones', default=0)

    class Meta:
        ordering = ['-num_views']
        verbose_name = 'Historial de Oferta'
        verbose_name_plural = 'Historial de Ofertas'

    def __str__(self):
        return 'Registro para \'%s\'' % self.offer


class UserOfferView(models.Model):

    user = models.ForeignKey(
        'customer.User', verbose_name='Usuario',
        on_delete=models.CASCADE)
    offer = models.ForeignKey(
        'catalogue.Offer',
        on_delete=models.CASCADE,
        verbose_name='Oferta')
    date_created = models.DateTimeField('Fecha de Creación', auto_now_add=True)

    class Meta:
        verbose_name = 'Visualización de Usuario-Oferta'
        verbose_name_plural = 'Visualizaciones de Usuario-Oferta'

    def __str__(self):
        return "%(user)s vió '%(offer)s'" % {
            'user': self.user, 'offer': self.offer}
