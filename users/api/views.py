from users.models import Profile, Message
from .serializers import ProfileSerailizer,MessageSerializer
from rest_framework import generics
# The urls for the below functions are defined in urls.py file

# To list of the userprofiles that are created using django signals 
# automatically as the user signs up
class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerailizer

# this is to get a single userprofile of just one user based on 
# the profile id 
class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerailizer
    lookup_field='seller'
    # though the seller id and profile id is different but here we 
    # access the profile based on the seller id

# this is if this user wants to update its profile
# using the patch request in profile.js
class ProfileUpdate(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerailizer
    lookup_field='seller'

# this is to list all the messages of the current user 
class MessageList(generics.ListAPIView):
    serializer_class = MessageSerializer
    # Extract recipient ID from the URL
    def get_queryset(self):
        recipient_id = self.kwargs.get("recipient_id")  
        return Message.objects.filter(recipient=recipient_id)

#this is to send the message and then serialize it 
class send_message(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

# to delete the message
class MessageDelete(generics.DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_field = "id"  # Not needed since we're overriding get_object

    def get_object(self):
        # get_queryset() returns a filtered queryset instead of a single object.
        # DestroyAPIView expects a single object to delete, but get_queryset() returns a list of objects (queryset)
        recipient_id = self.kwargs.get("recipient_id")
        message_id = self.kwargs.get("message_id")

        return Message.objects.get(id=message_id, recipient_id=recipient_id)
