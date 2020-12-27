from django.db import models

# Create your models here.

class Leaders(models.Model):
    name = models.CharField(max_length=140)
    image = models.FileField(upload_to="images/")
    designation = models.CharField(max_length=140)
    abbr = models.CharField(max_length=140)
    featured = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return self.name