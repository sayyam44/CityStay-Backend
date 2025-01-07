from rest_framework import serializers
from users.models import Profile

# to serialize the profile models into the readable format
class ProfileSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields = "__all__"

# serailizers implementation in users->views.py 
