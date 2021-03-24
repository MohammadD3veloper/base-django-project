from django.contrib import admin
from .models import Category, SubCategory, Post, Page

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['show_image', 'name', 'show_category', 'show_subcategory', 'show_author', 'date_create', 'date_update']
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['show_image', 'name', 'slug']
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'show_parent']
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title','date_create','date_update']