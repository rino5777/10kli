from django.contrib import admin
from .models import Category, Subcategory, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'slug')
    list_filter = ('category', 'name')
    
    prepopulated_fields = {'slug': ('name',)}



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =('name',  'subcategory', 'slug',  'available')
    list_filter = ('subcategory', 'available')
    list_editable = ( 'slug',  'subcategory', 'available')
    prepopulated_fields = {'slug': ('name',)}
