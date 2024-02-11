from django.contrib import admin
from .models import Products, Order


admin.site.site_header = "Ecommerce site"
admin.site.site_title = "Ecommerce site"
admin.site.index_title = "Manage ABC shopping"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')


admin.site.register(Products, ProductAdmin)
admin.site.register(Order)
