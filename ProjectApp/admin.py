from django.contrib import admin
from .models import Avto

class AvtoAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  
    search_fields = ('name',)  
    list_filter = ('name',)  

admin.site.register(Avto, AvtoAdmin)
