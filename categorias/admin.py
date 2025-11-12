from django.contrib import admin
from .models import Category

#admin.site.register(Category)

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ("title","description",)
    list_filter= ("title",)
    prepopulated_fields = {"slug":("title",)}
    search_fields = ("title", "description",)