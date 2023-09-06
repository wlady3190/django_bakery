from django.contrib import admin
from .models import Chef 
# Register your models here.

class ChefAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')


admin.site.register(Chef, ChefAdmin)