from rest_framework import serializers
from users.models import Profile,Message
#here we are importing the listing model to calculate the number of 
# listings for each user
from listings.models import Listing 
#here we are serializing the above listing model using the 
#already created listing_serailizer
from listings.api.serializers import ListingSerializer

# to serialize the profile models into the readable format
class ProfileSerailizer(serializers.ModelSerializer):

   #this is to add a column in the profiles models to get all the
   # listings of the particular seller along with 
   # the profile model using the listing model and then serializing it
    seller_listings = serializers.SerializerMethodField()
    def get_seller_listings(self,obj):
        query = Listing.objects.filter(seller=obj.seller); #this holds all the listings of the current seller
        listings_serialized=ListingSerializer(query, many=True) #this serialized the listing model
        return listings_serialized.data
    
    class Meta:#this holds all the data of the profile in models.py
        model=Profile
        fields = "__all__"

# serialize the messages model
# class MessageSerializer(serializers.ModelSerializer):
#     # Add a field to get all the messages for a user
#     user_messages = serializers.SerializerMethodField()

#     def get_user_messages(self, obj):
#         # Assuming obj is the Profile instance, and we want to get all messages for that user
#         # Filter messages where the user is either the sender or recipient
#         query = Message.objects.filter(sender=obj).all() | Message.objects.filter(recipient=obj).all()
#         messages_serialized = MessageSerializer(query, many=True)
#         return messages_serialized.data

#     class Meta:
#         model = Message
#         fields = ['id', 'sender', 'recipient', 'subject', 'body', 'is_read', 'created', 'user_messages']
#         # read_only_fields = ['created']# serailizers implementation in users->views.py 
class MessageSerializer(serializers.ModelSerializer):
    message_sender_name = serializers.CharField(source='sender.username', read_only=True)
    class Meta:
        model = Message
        # fields = "__all__"
        # read_only_fields = ['created']# serailizers implementation in users->views.py 
        fields = ['id', 'sender', 'recipient', 'subject', 'body', 'is_read', 'created', 'message_sender_name']
