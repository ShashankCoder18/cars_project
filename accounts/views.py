from django.shortcuts import render , redirect ,get_object_or_404 
from django.contrib import messages , auth

from django.contrib.auth.models import User 
from offices.models import Office
from listings.models import Listing

from .models import Order

# Create your views here.

def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        username  = request.POST['username']
        email      = request.POST['email']
        password   = request.POST['password']
        password2  = request.POST['password2']

        # Validations

        if password == password2:                                                   # 1. Check if Passswords match
                 
          if User.objects.filter(username=username).exists():                       # 2. Check For a unique username
           
            messages.error(request,'The Username is Already Taken !')               # Username is already taken 
            return redirect('register')
          
          else:
            if User.objects.filter(email=email).exists():                           # check for unique email 
             
              messages.error(request,'The email is used by another user!')          # Email is already being used    
              return redirect('register')

            else:                                                                   # Succesful register !! 
               user = User.objects.create_user(username=username, password=password,
                        email=email,first_name=first_name,last_name=last_name)
               user.save()
               messages.success(request,'You are Registered And can now Login !')
               return redirect('login')         

        else:                                                                       # If Passwords do not match     
          messages.error(request,'Passwords Do Not Match !')
          return redirect('register')
    
    else:                                                                           # If It's not a Post request
      return render(request,'accounts/register.html')                               

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
          auth.login(request, user)
          messages.success(request,'You are now logged in')
          return redirect('login')
        else:
          messages.error(request,'Invalid Credentials')
          return redirect('login')    
    else: 
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
      auth.logout(request)
      messages.success(request, 'You are Logged Out !')
      return redirect('index')

def dashboard(request):
    if request.method == 'POST':

      username   = request.POST['username']
      listing    = request.POST['listing']
      listing_id = request.POST['listing_id']
      office     = request.POST['office']
      company    = request.POST['company']
      email      = request.POST['email']
      address    = request.POST['address']
      phone      = request.POST['phone']
      pincode    = request.POST['pincode']
      payment    = request.POST['payment']

      order = Order( username=username , listing=listing , listing_id=listing_id ,office=office , company=company ,
                     email=email, address=address , phone=phone , pincode=pincode , payment=payment ) 

      order.save()               

      messages.success(request, ' Your Order Has Been Placed !')
      return redirect('dashboard')
    
    else:
      orders = Order.objects.order_by('-list_date').filter(username=request.user.username)  

      context={
        'orders' : orders
      }

      return render(request,'accounts/dashboard.html' , context )            

def checkout(request,listing_id):
    
      listing = get_object_or_404(Listing , pk = listing_id)

      context = {
          'listing': listing
      }

      return render(request,'accounts/checkout.html',context)    