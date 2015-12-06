from django.contrib import admin
from products.models import *
from onlineShop.utils.helper import *

class ProductAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.save()
        publishToFacebook(obj)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(CategoryLevel2)
admin.site.register(Image)
admin.site.register(SlideImage)
