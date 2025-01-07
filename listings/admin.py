from django.contrib import admin
from listings.models import Listing 
# from .forms import ListingsForm

#this is because we cannot directly register the models that are crreated in forms.py file
# class ListingAdmin(admin.ModelAdmin):
#     form=ListingsForm

# admin.site.register(Listing,ListingAdmin)
admin.site.register(Listing)