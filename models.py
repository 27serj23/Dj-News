from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')