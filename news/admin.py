from django.contrib import admin
from .models import Category, News

# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('slug', 'category__name', 'published_time')
    list_filter = ('category', 'published_time')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_time'
    search_fields = ('title', 'subtitle', 'description')
    ordering = ('-published_time',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)