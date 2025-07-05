from django.contrib import admin
from .models import Product, Profile,Category ,color,ssd,biz
from .models import Comment
# Register your models here.
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(color)
admin.site.register(ssd)
admin.site.register(biz)



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'created_at')
    list_filter = ('product', 'created_at')
