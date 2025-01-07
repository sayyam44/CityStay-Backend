from rest_framework import serializers 
from listings.models import Listing

class ListingSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    #this is because we need to get the seller(username) for each listing
    seller_username = serializers.SerializerMethodField() 
    # for getting the having a user profile for each user 
    seller_agency_name=serializers.SerializerMethodField()

    def get_seller_agency_name(self,obj): #this is to serialize the models for the user's profile
        return obj.seller.profile.agency_name

    def get_country(self,obj):
        return "Canada"
    
    def get_seller_username(self,obj):
        return obj.seller.username
    
    class Meta: #here whole models.py file is being serialized as it is
        model=Listing
        fields = '__all__'
