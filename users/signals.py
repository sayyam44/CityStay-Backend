from .models import Profile
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver 
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings 

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

        subject = "Welcome to CityStayNL!"
        body = f"Hi , Welcome to CityStayNL! We're excited to have you on board."
        from_email = "admin@citystaynl.com"  # You can set this as your 'DEFAULT_FROM_EMAIL'

        # Send email using SendGrid
        message = Mail(
            from_email=from_email,
            to_emails=instance.email,
            subject=subject,
            plain_text_content=body
        )

        try:
            # Use the SendGrid API key from your settings
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(message)
            print(f"Email sent with status code: {response.status_code}")
        except Exception as e:
            print(f"Error sending email: {e}")

# above function creates the profile now the below function saves 
# this profile
@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()


#To connect these signals implement in user->apps.py 