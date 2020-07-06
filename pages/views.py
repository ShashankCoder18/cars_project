from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import pricec ,companyc, showroomc ,seatsc

from listings.models import Listing

# Create your views here.
def main(request):
    return render(request,'pages/main.html')

def index(request):
    listings =  Listing.objects.order_by('-rating').filter(is_available=True) [:3]
    
    context = {
        'listings': listings,
        'pricec' : pricec,
        'companyc' : companyc,
        'showroomc' : showroomc,
        'seatsc' : seatsc,
    }
    return render(request,'pages/index.html',context)

def about(request):
    return render(request,'pages/about.html')


        