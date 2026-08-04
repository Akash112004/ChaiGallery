from django.contrib import admin

# Register your models here.

from .models import Tea


@admin.register(Tea)
class TeaAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at',)