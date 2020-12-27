from django.contrib import admin
from .models import Dishes # add this
class DishesAdmin(admin.ModelAdmin):  # add this
  list_display = ('name', 'image', 'description', 'label', 'featured', 'price', 'category') # add this


# Register your models here.
admin.site.register(Dishes, DishesAdmin) # add this
