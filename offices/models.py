from django.db import models

# Create your models here.

class Office(models.Model):
    oname = models.CharField(max_length=200)
    address = models.CharField(max_length=250)
    area = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',blank = True)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    def __str__(self):
        return self.oname