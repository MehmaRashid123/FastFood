from django.contrib import admin
from .models import MenuItem, Deal

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_available', 'created_at')
    list_filter = ('is_available',)
    search_fields = ('name', 'description')


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('title', 'original_price', 'discounted_price', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('title',)