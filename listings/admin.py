from django.contrib import admin
from listings.models import Listing,Poi,Review
#registering the new models created in models.py
from .forms import PoisForm

#this is because we cannot directly register the models 
#that we created in forms.py file
class PoiAdmin(admin.ModelAdmin):
    form=PoisForm
# register Poi model and PoiAdmin
admin.site.register(Poi,PoiAdmin)

#register the listing model
admin.site.register(Listing)

#register the review model
admin.site.register(Review)