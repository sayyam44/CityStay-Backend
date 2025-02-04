from rest_framework import serializers 
from listings.models import Listing,Poi,Review
# using GeoDjango library to filter the pois upto 2km for each listing
from django.contrib.gis.measure import D  # ``D`` is a shortcut for ``Distance``
from django.contrib.gis.geos import Point

# serializin the Listing model
class ListingSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    #this is because we need to get the seller(username) for each listing
    seller_username = serializers.SerializerMethodField() 
    # for having a user profile(agency name) for each user 
    seller_agency_name=serializers.SerializerMethodField()
    # for having the all pois for each listing within 2kms
    listing_pois_within_2km=serializers.SerializerMethodField()
    # for having all the reviews for each listing
    reviews = serializers.SerializerMethodField() 

    # this is to get all the pois for a listing within 2kms
    def get_listing_pois_within_2km(self,obj):
        #here we are storing the location of the current location in point object
        listing_location=Point(obj.latitude,obj.longitude,srid=4326) 
        #this gets all the pois of current lisiting with 2km 
        # location in location__distance__lte is the location field of pois in model
        #distance__lte=>at a distance of less than or equal to
        # listing_location=>It hold the location of the current listing
        query = Poi.objects.filter(location__distance_lte=(listing_location,D(km=2))) 
        query_serialized=PoiSerializer(query,many=True)
        return query_serialized.data
    
    # Fetch all reviews related to the listing
    def get_reviews(self, obj):
        reviews = obj.reviews.all() 
        review_serializer = ReviewSerializer(reviews, many=True)
        return review_serializer.data

    #this is to serialize the models for the username of each listing
    def get_seller_username(self,obj):
        return obj.seller.username
    
    #this is to serialize the models for the user's profile(agency name) for each listing
    def get_seller_agency_name(self,obj): 
        return obj.seller.profile.agency_name

    def get_country(self,obj):
        return "Canada"
    
    class Meta: #here whole models.py file is being serialized as it is
        model=Listing
        fields = '__all__'

# Serializing the Poi Model
class PoiSerializer(serializers.ModelSerializer):
    class Meta:
        model=Poi
        fields='__all__'

# Serializing the Review model by adding the review_username field
class ReviewSerializer(serializers.ModelSerializer):
    review_username = serializers.CharField(source='user.username', read_only=True)  # Display username of the reviewer

    class Meta:
        model = Review
        # fields='__all__'
        fields = ['date_posted','id','listing','rating', 'review','user','review_username']
