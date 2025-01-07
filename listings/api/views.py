from .serializers import ListingSerializer
from listings.models import Listing
from rest_framework import generics
# generics are a set of pre-built views that provide common patterns 
# for building APIs, such as creating, retrieving, updating, and
# deleting resources. They allow you to handle CRUD operations with 
# minimal code by leveraging DRF's robust class-based view (CBV) 
# system.
# The urls for the below functions are defined in urls.py file

# to list the listing 
class ListingList(generics.ListAPIView):
    queryset=Listing.objects.all().order_by('-date_posted')
    serializer_class = ListingSerializer

# to create a new listing from frontend from AddProperty.js 
class ListingCreate(generics.CreateAPIView):
    queryset=Listing.objects.all()
    serializer_class = ListingSerializer

