from django.db import models
from dish.models import Dishes
# Create your models here.
class Comments(models.Model):
    dishId = models.ForeignKey(Dishes, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    author = models.CharField(max_length=140)
    date = models.DateTimeField()

    def _str_(self):
        return self.comment