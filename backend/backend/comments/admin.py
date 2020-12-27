from django.contrib import admin
from .models import Comments
# Register your models here.
class CommentsAdmin(admin.ModelAdmin):
    list_display=('dishId', 'rating', 'comment', 'author','date')

admin.site.register(Comments, CommentsAdmin) # add this