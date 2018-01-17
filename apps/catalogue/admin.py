from django.contrib import admin

from .models import Product, Coupon, Category

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "category", "updated", "timestamp"]
    list_display_links = ["updated"]
    list_editable = ["title", "description"]
    list_filter = ["category", "updated", "timestamp"]
    search_fields = ["title", "description"]

    class Meta:
        model = Product


class CouponModelAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "valid_until","updated","timestamp"]
    list_display_links = ["updated"]
    list_editable = ["title", "description", "valid_until"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "description"]

    class Meta:
        model = Coupon


admin.site.register(Product, ProductModelAdmin)
admin.site.register(Coupon, CouponModelAdmin)
#admin.site.register(Category)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'name')
    search_fields = ('name', 'category__name')


