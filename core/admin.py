from django.contrib import admin

from django.contrib.admin import TabularInline
from core.models import Product, ApplicationCall, ToNotification

admin.site.register(ApplicationCall)
admin.site.register(ToNotification)
admin.site.register(Product)


# class ProductPhotoAdmin(TabularInline):
#     fields = ['product', 'photo', 'is_main']
#     model = ProductPhoto

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['title', 'description']
#     inlines = ProductPhotoAdmin,
 