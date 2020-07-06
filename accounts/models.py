from django.db import models
from datetime  import datetime
from companies.models import Company 
from offices.models import Office
from listings.models import Listing

# Create your models here.

class Order(models.Model):
    username   = models.CharField(max_length=200)
    listing    = models.CharField(max_length=200) 
    listing_id = models.IntegerField()
    office     = models.CharField(max_length=200)
    company    = models.CharField(max_length=200)
    email      = models.CharField(max_length=200)
    address    = models.TextField()
    phone      = models.IntegerField()
    pincode    = models.IntegerField()
    payment    = models.CharField(max_length=200)
    list_date  = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.listing

    
