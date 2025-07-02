from django.contrib import admin
from .models import Product, Profile,Category ,color,ssd

# Register your models here.
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(color)
admin.site.register(ssd)