from users.models import Profile
from .serializers import ProfileSerailizer
from rest_framework import generics
# The urls for the below functions are defined in urls.py filee
#new
# To list the userprofiles that are created using django signals 
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

# this is if the user wants to update its profile
# using the patch request in profile.js
class ProfileUpdate(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerailizer
    lookup_field='seller'

# The urls for the functions are defined in urls.py file
