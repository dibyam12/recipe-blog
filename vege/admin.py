from django.contrib import admin
from .models import *




class RecipeAdmin(admin.ModelAdmin):
    list_display = ('user','name','description','image','is_shared')

admin.site.register(Recipe,RecipeAdmin)
# Register your models here.
