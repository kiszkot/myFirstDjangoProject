from django.contrib import admin
from .models import CEO, Recipe, Restaurant, Chef

# Register your models here.

admin.site.register(CEO)
admin.site.register(Recipe)
admin.site.register(Restaurant)
admin.site.register(Chef)