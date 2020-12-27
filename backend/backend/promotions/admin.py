from django.contrib import admin
from .models import Promotions # add this
class PromotionsAdmin(admin.ModelAdmin):  # add this
  list_display = ('name', 'image', 'label', 'price', 'featured', 'description') # add this


# Register your models here.
admin.site.register(Promotions, PromotionsAdmin) # add this
