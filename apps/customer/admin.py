from django.contrib import admin

from .models import User


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'first_name', 'last_name', 'email', 'password', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    list_display = ('username', 'first_name', 'last_name', 'email')

    def save_model(self, request, obj, form, change):
        user = request.user
        super().save_model(request, obj, form, change)
