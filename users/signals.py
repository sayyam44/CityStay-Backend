from .models import Profile
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver 

User = get_user_model()
# in models.py file we originally have 2 models 1)usermodel 2)profile model
# Here we are using django post_save signal to create a profile 
# for each user who is logged in 

# When the user is saved then the usermodel sends a postsave signal to the 
# the receiver that then performs a task , and that task is defined
# as a function to create a user profile 
@receiver(post_save,sender=User)
# these arguments in the below function comes from the post_save signal
# sender -> usermodel, instance->is an instance of the user model
# created-->Boolean value
def create_user_profile(sender, instance, created, **kwargs):
    if created:  #If the user model instance(new user) is created 
        #then we are creating a new object i.e. model(userprofile)
        # for that newly created user
        Profile.objects.create(seller=instance) 


# above function creates the profile now the below function saves 
# this profile
@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()


#To connect these signals implement in user->apps.py 