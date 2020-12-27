from django.db import models

# Create your models here.
class Promotions(models.Model):
    name = models.CharField(max_length=140)
    image = models.FileField(upload_to="images/")
    label = models.CharField(max_length=140)
    featured = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name