from django.db import models

# Create your models here.

class store(models.Model):
    img_name = models.CharField(max_length=200)
    img_file = models.ImageField(upload_to='images',blank=True)

