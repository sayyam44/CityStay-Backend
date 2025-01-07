from django.db import models
from django.contrib.auth.models import AbstractUser

# This User model inherits from AbstractUser, which means it has all 
# the built-in fields like username, email, password, etc., plus any 
# additional fields you define 
class User(AbstractUser):
    email = models.EmailField(unique=True)
# Wherever you need to refer to the this User model use get_user_model() 
# to get the custom user model eg in users->admin.py and listings->models.py

class Profile(models.Model):
    #seller field is the user of this profile
    seller = models.OneToOneField(User, on_delete=models.CASCADE)
    agency_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=25, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return f"Profile of {self.seller.username}"