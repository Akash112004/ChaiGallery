from django.contrib import admin
from .models import Tea
# Register your models here.






@admin.register(Tea)
class TeaAdmin(admin.ModelAdmin):
    list_display = ('user','name', 'created_at', 'updated_at')
    search_fields = ('user', 'name',)
    list_filter = ('created_at',)