from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# This User model inherits from AbstractUser, which means it has all 
# the built-in fields like username, email, password, etc., plus any 
# additional fields you define 
class User(AbstractUser): #this is associated with each user
    email = models.EmailField(unique=True)
# Wherever you need to refer to the this User model use get_user_model() 
# to get the custom user model eg in users->admin.py and listings->models.py

class Profile(models.Model): #this is assocciated with each profile of the user 
    #seller field is the userid of this profile
    # we will access the profile/agency in the basis of this
    # seller(user) id not on the basis of the profile id
    # that logic is written in urls.py file
    seller = models.OneToOneField(User, on_delete=models.CASCADE)
    agency_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=25, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return f"Profile of {self.seller.username}"

class Message(models.Model):
    sender = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    recipient = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True, related_name="messages")
    # name = models.CharField(max_length=200, null=True, blank=True)
    # email = models.CharField(max_length=200,null=True, blank=True)
    subject = models.CharField(max_length=200,null=True, blank=True)
    body = models.TextField()
    is_read= models.BooleanField(default=False,null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subject if self.subject else f"Message from {self.sender} to {self.recipient}"