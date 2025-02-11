from .serializers import ListingSerializer,ReviewSerializer
from listings.models import Listing,Review
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
User = get_user_model()
# generics are a set of pre-built views that provide common patterns 
# for building APIs, such as creating, retrieving, updating, and
# deleting resources. They allow you to handle CRUD operations with 
# minimal code by leveraging DRF's robust class-based view (CBV) 
# system.
# The urls for the below functions are defined in urls.py file

# to show all the listings 
class ListingList(generics.ListAPIView):
    queryset=Listing.objects.all().order_by('-date_posted')
    serializer_class = ListingSerializer
 
# to create a new listing from frontend from AddProperty.js 
class ListingCreate(generics.CreateAPIView):
    queryset=Listing.objects.all()
    serializer_class = ListingSerializer

# to get the detail of each listing 
class ListingDetail(generics.RetrieveAPIView):
    queryset=Listing.objects.all()
    serializer_class = ListingSerializer

# to delete the current listing used in listingdetail.js
class ListingDelete(generics.DestroyAPIView):
    queryset=Listing.objects.all()
    serializer_class = ListingSerializer

#to update the current listing 
class ListingUpdate(generics.UpdateAPIView):
    queryset=Listing.objects.all()
    serializer_class = ListingSerializer


class AddReview(generics.CreateAPIView):
    queryset = Review.objects.all().order_by('-date_posted')
    serializer_class = ReviewSerializer

    # def perform_create(self, serializer):
    #     # listing_id = self.request.data.get('listing_id')
    #     user_id = self.request.data.get('user_id')

    #     try:
    #         # listing = Listing.objects.get(id=listing_id)
    #         user = User.objects.get(id=user_id)
    #     except (Listing.DoesNotExist, User.DoesNotExist):
    #         raise ValidationError({"error": "Invalid listing_id or user_id"})

    #     serializer.save(user=user)
