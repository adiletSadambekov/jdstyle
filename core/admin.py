from django.contrib import admin

from django.contrib.admin import TabularInline
from core.models import Product, ApplicationCall, ToNotification, Category, Sizes

admin.site.register(ApplicationCall)
admin.site.register(ToNotification)
admin.site.register(Product)
# admin.site.register(Category)
admin.site.register(Sizes)


# class ProductPhotoAdmin(TabularInline):
#     fields = ['product', 'photo', 'is_main']
#     model = ProductPhoto

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['title', 'description']
#     inlines = ProductPhotoAdmin,
 