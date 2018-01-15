from django.contrib import admin

from .models import Product, Coupon, Category


admin.site.register(Product)
admin.site.register(Coupon)
#admin.site.register(Category)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'name')
    search_fields = ('name', 'category__name')