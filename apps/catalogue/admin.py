'''
To Manage the forms for produc, cotegory and promotion models.
'''
from django.contrib import admin, messages
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string

from sorl.thumbnail import get_thumbnail

from .models import Product, Coupon, Category, Offer


User = get_user_model()


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    '''ModelAdmin of Product'''
    fieldsets = (
        (None, {'fields': ('title', 'description', 'image', 'category')}),
    )
    list_display = ('title', 'description', 'get_image', 'modified_user',
                    'created_user', 'modified_at', 'created_at')
    list_filter = ('category',)
    search_fields = ('title',)

    def get_image(self, obj):
        '''Returns the image as thumbnail in the admin'''
        img = ''
        if obj.image:
            thumb = get_thumbnail(obj.image, '80x80')
            img = '<center><a href={0}><img src="{0}"/></a></center>'\
                  .format(thumb.url)
        return img
    get_image.allow_tags = True
    get_image.short_description = 'Imagen'

    def save_model(self, request, obj, form, change):
        user = request.user
        if not obj.id:
            obj.created_user = user
        obj.modified_user = user
        super().save_model(request, obj, form, change)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Registration of the Category Model'''

    fieldsets = (
        (None, {'fields': ('name', 'image')}),
    )
    list_display = ('name', 'get_image', 'modified_user', 'created_user',
                    'modified_at', 'created_at')
    search_fields = ('name',)

    def get_image(self, obj):
        '''Returns the image as thumbnail in the admin'''
        img = ''
        if obj.image:
            thumb = get_thumbnail(obj.image, '80x80')
            img = '<center><a href={0}><img src="{0}"/></a></center>'\
                  .format(thumb.url)
        return img
    get_image.allow_tags = True
    get_image.short_description = 'Imagen'

    def save_model(self, request, obj, form, change):
        user = request.user
        if not obj.id:
            obj.created_user = user
        obj.modified_user = user
        super().save_model(request, obj, form, change)


class PromotionModelAdmin(admin.ModelAdmin):
    '''
    Promotion Model to be inherit by ModelAdmin of Coupon and Offer
    '''

    fieldsets = (
        (None, {'fields': ('title', 'description', 'date_expiry', 'image')}),
    )
    list_display = ('title', 'description', 'get_image', 'modified_user',
                    'created_user', 'modified_at', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('modified_at', 'created_at')
    actions = ['enviar_email',]

    def get_image(self, obj):
        '''Returns the image as thumbnail in the admin'''
        img = ''
        if obj.image:
            thumb = get_thumbnail(obj.image, '80x80')
            img = '<center><a href={0}><img src="{0}"/></a></center>'\
                  .format(thumb.url)
        return img
    get_image.allow_tags = True
    get_image.short_description = 'Imagen'

    def save_model(self, request, obj, form, change):
        user = request.user
        if not obj.id:
            obj.created_user = user
        obj.modified_user = user
        super().save_model(request, obj, form, change)

    def enviar_email(self, request, queryset):
        if not queryset:
            messages.error(request, 'Error, se debe seleccionar uno o mas promociones')
        else:
            rendered = render_to_string('promotion/responsive.html', { 'promotion': queryset })
            receivers = User.objects\
                            .filter(is_active=True)\
                            .exclude(email='', is_staff=False)\
                            .values_list('email', flat=True)
            print(receivers)
            if receivers:
                send_mail('Nuevas Promociones', '', 'marketing@burgerking.com', 
                          receivers, html_message=rendered)

            messages.success(request, 'Se ha enviado el correo electrónico correctamente')
    send_mail.short_description='Enviar Correo Electrónico'
    send_mail.allow_tags = True


@admin.register(Coupon)
class CouponModelAdmin(PromotionModelAdmin):
    '''Registration of the Coupon Model in AdminModel'''
    pass

@admin.register(Offer)
class OfferModelAdmin(PromotionModelAdmin):
    '''Registration of the Offer Model in AdminModel'''
    pass
