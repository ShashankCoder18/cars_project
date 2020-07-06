from django.shortcuts import get_object_or_404 , render
from django.http import HttpResponse
from django.core.paginator import EmptyPage , PageNotAnInteger , Paginator
from listings.choices import pricec ,companyc, showroomc ,seatsc

from itertools import chain

from .models import Listing
from offices.models import Office
from companies.models import Company

# Create your views here.
def index(request):
    listings = Listing.objects.all().filter()

    paginator = Paginator( listings,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
 
    context = {
        'listings' : paged_listings
    }
    return render(request,'listings/listings.html',context)

def listing(request,listing_id):

    listing = get_object_or_404(Listing , pk = listing_id)
    query_list = Office.objects.order_by('oname')
    queryset_list = Listing.objects.order_by('office')
    queryset_list = queryset_list.filter(pk = listing_id)
    
    
    context = {
        'listing': listing,
        }

    return render(request,'listings/listing.html',context)    

def search(request):
    queryset_list = Listing.objects.order_by('company')
    q = Company.objects.order_by('cname')

    # Keywords
    if 'keywords' in request.GET:
      keywords =  request.GET['keywords']
      if keywords:
          queryset_list = queryset_list.filter(description__icontains=keywords)

    # Company
    if 'company' in request.GET:
      companys =  request.GET['company']
      if companys:
          queryset_list = queryset_list.filter(company=companys)      

    # Price 
    if 'price' in request.GET:
      price =  request.GET['price']
      if price:
          queryset_list = queryset_list.filter(price__lte=price) 
        
    # Showroom
    if 'showroom' in request.GET:
      showroom =  request.GET['showroom']
      if showroom:
          queryset_list = queryset_list.filter(office=showroom)    
    
    # Seats
    if 'seats' in request.GET:
      seats =  request.GET['seats']
      if seats:
          queryset_list = queryset_list.filter(seats__lte=seats)            

    context = {
        'pricec' : pricec,
        'companyc' : companyc,
        'showroomc' : showroomc,
        'seatsc' : seatsc,
        'listings' : queryset_list,
        'values' : request.GET
    }
    return render(request,'listings/search.html',context)    