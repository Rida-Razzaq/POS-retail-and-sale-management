from django.contrib import admin
from .models import Order, Product
from django.contrib.auth.models import Group

admin.site.site_header = 'POS website'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category' ,'quantity')
    list_filter = ['category']

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
#admin.site.unregister(Group)