from django.contrib import admin

from .models import data

# admin.site.register(data)
@admin.register(data)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    ordering = ('name',)
    search_fields = ('name', 'value')
