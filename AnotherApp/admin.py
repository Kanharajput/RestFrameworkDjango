from django.contrib import admin
from .models import *

admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


class BookInline(admin.TabularInline):
    model = Book

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [BookInline]
