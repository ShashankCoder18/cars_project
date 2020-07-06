from django.db import models

# Create your models here.

class Company(models.Model):
    cname = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',blank = True)
    description = models.TextField(blank=True)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    is_mvp = models.BooleanField(default=False)
    def __str__(self):
        return self.cname