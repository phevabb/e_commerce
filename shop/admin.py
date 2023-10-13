from django.contrib import admin

from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'category', 'available', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    list_filter =['available', 'created', 'updated']
    list_editable = [ 'available', 'price']




# Register your models here.
