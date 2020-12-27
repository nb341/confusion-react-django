from django.db import models
# Create your models here.

# add this
def directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'images/{0}.png'.format(filename)
class Dishes(models.Model):
  name = models.CharField(max_length=120)
  category = models.CharField(max_length=120)
  label = models.CharField(max_length=120)
  image = models.FileField(upload_to='images/')
  price = models.DecimalField(max_digits=10, decimal_places=2)
  featured = models.BooleanField(default=False)
  description = models.TextField()


  def _str_(self):
    return self.name

