from rest_framework import serializers
from users.models import Profile
#here we are importing the listing model to calculate the number of 
# listings for each user
from listings.models import Listing 
#here we are serializing the above listing model using the 
#already created listing_serailizer
from listings.api.serializers import ListingSerializer

# to serialize the profile models into the readable format
class ProfileSerailizer(serializers.ModelSerializer):

   #this is to get each listing of the seller along with the 
   # profile model using the listing model and then serializing it
    seller_listings = serializers.SerializerMethodField()
    def get_seller_listings(self,obj):
        query = Listing.objects.filter(seller=obj.seller); #this holds all the listings of the current seller
        listings_serialized=ListingSerializer(query, many=True) #this serialized the listing model
        return listings_serialized.data
    
    class Meta:#this holds all the data of the profile in models.py
        model=Profile
        fields = "__all__"

# serailizers implementation in users->views.py 
