from django.contrib import admin

from mainapp.models import Category, Model, Location

admin.site.register(Category)
admin.site.register(Model)
admin.site.register(Location)