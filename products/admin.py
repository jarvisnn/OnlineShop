from django.contrib import admin
from products.models import *

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(CategoryLevel2)
admin.site.register(Image)
admin.site.register(SlideImage)
