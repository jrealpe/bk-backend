from django.contrib import admin

from sorl.thumbnail import get_thumbnail

from .models import Product, Coupon, Category


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category', 'modified_at', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'description')


@admin.register(Coupon)
class CouponModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'get_image', 'modified_at', 'created_at')
    search_fields = ('title', 'description')

    def get_image(self, obj):
        img = ''
        if obj.image:
            thumb = get_thumbnail(obj.image, '80x80')
            img = '<center><a href={0}><img src="{0}"/></a></center>'\
                  .format(thumb.url)
        return img
    get_image.allow_tags = True
    get_image.short_description = 'Imagen'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'name')
    search_fields = ('name', 'category__name')
