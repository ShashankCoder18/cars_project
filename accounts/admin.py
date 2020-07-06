from django.contrib import admin

from .models import Order

# Register your models here.

class Orders(admin.ModelAdmin):
    list_display = ('id' , 'listing' , 'username' , 'list_date')
    list_display_links = ('id' , 'listing')
    search_fields = ('username' , 'email' , 'listing'  )
    list_per_page = 25
      
admin.site.register(Order,Orders)    