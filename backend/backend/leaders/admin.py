from django.contrib import admin
from .models import Leaders # add this
class LeadersAdmin(admin.ModelAdmin):  # add this
  list_display = ('name', 'image', 'abbr', 'designation', 'featured', 'description') # add this


# Register your models here.
admin.site.register(Leaders, LeadersAdmin) # add this
