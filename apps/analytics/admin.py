'''
To Manage the admin for analytics models.
'''

from django.contrib import admin

from import_export import admin as ie_admin
from import_export import resources

from .models import *

from apps.catalogue.models import Category



class UserRecordResource(resources.ModelResource):

    class Meta:
        model = UserRecord
        skip_unchanged = True
        report_skipped = False
        fields = ('id', 'user__first_name', 'user__last_name',
                  'num_product_views', 'num_offer_views', 'num_coupon_views')
        export_order = fields


class ProductRecordResource(resources.ModelResource):

    class Meta:
        model = ProductRecord
        skip_unchanged = True
        report_skipped = False
        fields = ('id', 'product__title', 'num_views')
        export_order = fields


class UserProductViewResource(resources.ModelResource):

    class Meta:
        model = UserProductView
        skip_unchanged = True
        report_skipped = False
        fields = ('id', 'user__first_name', 'user__last_name', 
                  'product__title', 'date_created')
        export_order = fields


class CouponRecordResource(resources.ModelResource):

    class Meta:
        model = CouponRecord
        skip_unchanged = True
        report_skipped = False
        fields = ('id', 'coupon__title', 'num_views')
        export_order = fields


class UserCouponViewResource(resources.ModelResource):

    class Meta:
        model = UserCouponView
        skip_unchanged = True
        report_skipped = False
        fields = ('id', 'user__first_name', 'user__last_name', 
                  'coupon__title', 'date_created')
        export_order = fields


class OfferRecordResource(resources.ModelResource):

    class Meta:
        model = OfferRecord
        skip_unchanged = True
        report_skipped = False
        fields = ('id', 'offer__title', 'num_views')
        export_order = fields


class UserOfferViewResource(resources.ModelResource):

    class Meta:
        model = UserOfferView
        skip_unchanged = True
        report_skipped = False
        fields = ('id', 'user__first_name', 'user__last_name', 
                  'offer__title', 'date_created')
        export_order = fields


#################
# Filters Admin #
#################

class CategoryFilter(admin.SimpleListFilter):
    title = 'Categoría'
    parameter_name = 'category'

    def lookups(self, request, model_admin):
        return [(c.id, c.name) for c in Category.objects.all()]


class ProductCategoryFilter(CategoryFilter):

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(product__category__id__exact=self.value())
        else:
            return queryset


################
# Models Admin #
################

class AnalyticsModelAdmin(ie_admin.ImportExportActionModelAdmin, 
                          admin.ModelAdmin):
    pass


@admin.register(UserRecord)
class UserRecordModelAdmin(AnalyticsModelAdmin):
    '''ModelAdmin of UserRecord'''
    list_display = ('user', 'num_product_views', 'num_coupon_views', 
                    'num_offer_views')
    search_fields = ('user__username', 'user__email', 'user__first_name',
                     'user__last_name')
    resource_class = UserRecordResource


@admin.register(ProductRecord)
class ProductRecordModelAdmin(AnalyticsModelAdmin):
    '''ModelAdmin of ProductRecord'''
    list_display = ('product', 'num_views')
    list_filter = (ProductCategoryFilter,)
    search_fields = ('product__title',)
    resource_class = ProductRecordResource


@admin.register(UserProductView)
class UserProductViewModelAdmin(AnalyticsModelAdmin):
    '''ModelAdmin of UserProductView'''
    list_display = ('user', 'product', 'date_created')
    list_filter = (ProductCategoryFilter,)
    search_fields = ('product__title',)
    resource_class = UserProductViewResource


@admin.register(CouponRecord)
class CouponRecordModelAdmin(admin.ModelAdmin):
    '''ModelAdmin of CouponRecord'''
    list_display = ('coupon', 'num_views')
    search_fields = ('coupon__title',)
    resource_class = CouponRecordResource


@admin.register(UserCouponView)
class UserCouponViewModelAdmin(admin.ModelAdmin):
    '''ModelAdmin of UserCouponView'''
    list_display = ('user', 'coupon', 'date_created')
    search_fields = ('coupon__title',)
    resource_class = UserCouponViewResource


@admin.register(OfferRecord)
class OfferRecordModelAdmin(admin.ModelAdmin):
    '''ModelAdmin of OfferRecord'''
    list_display = ('offer', 'num_views')
    search_fields = ('offer__title',)
    resource_class = OfferRecordResource


@admin.register(UserOfferView)
class UserOfferViewModelAdmin(admin.ModelAdmin):
    '''ModelAdmin of UserOfferView'''
    list_display = ('user', 'offer', 'date_created')
    search_fields = ('offer__title',)
    resource_class = UserOfferViewResource
