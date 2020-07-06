from django.db import models
from datetime  import datetime
from companies.models import Company 
from offices.models import Office

# Create your models here.

class Listing(models.Model):
    company = models.ForeignKey(Company, on_delete = models.DO_NOTHING)
    office  = models.ForeignKey(Office, on_delete = models.DO_NOTHING)
    name = models.CharField(max_length = 200)
    category = models.CharField(max_length = 200)
    description = models.TextField(blank = True)
    price = models.IntegerField()
    seats = models.IntegerField()
    colour = models.CharField(max_length = 200)
    colour1 = models.CharField(max_length = 200,blank = True)
    colour2 = models.CharField(max_length = 200,blank = True)
    rating = models.IntegerField() 
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/',blank = True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank = True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank = True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank = True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank = True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank = True) 
    is_available = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.name