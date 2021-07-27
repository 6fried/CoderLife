from django.contrib import admin
from .models import Showcase

class ShowcaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'content')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('created_at',)

admin.site.register(Showcase, ShowcaseAdmin)