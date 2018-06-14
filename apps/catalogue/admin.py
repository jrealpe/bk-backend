'''
To Manage the forms for produc, cotegory and promotion models.
'''
from django.contrib import admin

from sorl.thumbnail import get_thumbnail

from .models import Product, Coupon, Category, Offer


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


@admin.register(Coupon)
class CouponModelAdmin(PromotionModelAdmin):
    '''Registration of the Coupon Model in AdminModel'''
    pass

@admin.register(Offer)
class OfferModelAdmin(PromotionModelAdmin):
    '''Registration of the Offer Model in AdminModel'''
    pass
