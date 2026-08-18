from django.contrib import admin

# Register your models here.

from .models import Tea


@admin.register(Tea)
class TeaAdmin(admin.ModelAdmin):
    list_display = ('user','name', 'created_at', 'updated_at')
    search_fields = ('user', 'name',)
    list_filter = ('created_at',)