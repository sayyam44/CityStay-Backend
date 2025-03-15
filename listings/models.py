from random import choices
from django.contrib.gis.db import models
from django.utils import timezone
from django.contrib.gis.geos import Point

from django.contrib.auth import get_user_model
User = get_user_model()

from django.core.files import File
import PIL #The Pillow (PIL) library in Python is used for image processing. 
from io import BytesIO #this library in Python provides an in-memory binary stream that behaves like a file. It allows you to read and write binary data (bytes) without actually using disk storage.
# Stores binary data in memory (RAM) instead of writing to disk.

def compress(picture):
    if picture:
        pic=PIL.Image.open(picture)
        buf=BytesIO()
        pic.save(buf, 'JPEG', quality=60)
        new_pic=File(buf,name=picture.name)
        return new_pic
    else:
        return None


#model for lisitngs
class Listing(models.Model):
    seller= models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    choices_area = (
    ("Inner St.John's", "Inner St.John's"),
    ("Outer St.John's", "Outer St.John's"),
    )
    area = models.CharField(max_length=20, blank=True,
                            null=True, choices=choices_area)
    borough = models.CharField(max_length=50, blank=True, null=True)
    choices_listing_type = (
        ('House', 'House'),
        ('Apartment', 'Apartment'),
        ('Office', 'Office'),
    )
    listing_type = models.CharField(
        max_length=20, choices=choices_listing_type)
    choices_property_status = (
        ('Sale', 'Sale'),
        ('Rent', 'Rent'),
    )
    property_status = models.CharField(
        max_length=20, blank=True, null=True, choices=choices_property_status)
    price = models.DecimalField(max_digits=50, decimal_places=0)
    choices_rental_frequency = (
        ('Month', 'Month'),
        ('Week', 'Week'),
        ('Day', 'Day'),
    )
    rental_frequency = models.CharField(
        max_length=20, blank=True, null=True, choices=choices_rental_frequency)
    rooms = models.IntegerField(blank=True, null=True)
    furnished = models.BooleanField(default=False)
    # pool = models.BooleanField(default=False)
    utilities = models.BooleanField(default=False)
    # elevator = models.BooleanField(default=False)
    petfriendly = models.BooleanField(default=False)
    cctv = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    address = models.CharField(max_length=150, default="Not Provided")
    date_posted = models.DateTimeField(default=timezone.now)
    # location = models.PointField(blank=True, null=True,srid=4326)
    latitude=models.FloatField(blank=True,null=True)
    longitude=models.FloatField(blank=True,null=True)
    picture1= models.ImageField(blank=True,null=True,upload_to="pictures/%Y/%m/%d/")
    picture2= models.ImageField(blank=True,null=True,upload_to="pictures/%Y/%m/%d/")
    picture3= models.ImageField(blank=True,null=True,upload_to="pictures/%Y/%m/%d/")
    picture4= models.ImageField(blank=True,null=True,upload_to="pictures/%Y/%m/%d/")
    picture5= models.ImageField(blank=True,null=True,upload_to="pictures/%Y/%m/%d/")
    
    # for returning the value of the title field as the string
    def __str__(self):
        return self.title    

    def save(self, *args, **kwargs):
        new_picture1=compress(self.picture1)
        self.picture1=new_picture1
        new_picture2=compress(self.picture2)
        self.picture2=new_picture2
        new_picture3=compress(self.picture3)
        self.picture3=new_picture3
        new_picture4=compress(self.picture4)
        self.picture4=new_picture4
        new_picture5=compress(self.picture5)
        self.picture5=new_picture5
        super().save(*args,**kwargs)


#model for point of interest 
class Poi(models.Model):
    name = models.CharField(max_length=120, blank=True)
    choices_type=(
        ('University', 'University'),
        ('Hospital', 'Hospital'),
        ('Stadium', 'Stadium'),
        ('Mall','Mall'),
        ('College','College'),
    )
    type = models.CharField(max_length=50, choices=choices_type)

    #since we need to apply the distance fiters so that is why 
    #we cannot use latitute, logintude seperately we used PointField
    # To save latitude,longitude in location array we use forms.py
    location = models.PointField(blank=True, null=True,srid=4326)

    # for returning the value of the name field as the string
    def __str__(self):
        return self.name 


class Review(models.Model):
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # THIS IS TO ADD A RATING FROM 0 TO 5 STARS.
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(0, 6)], default=5)  # Rating from 1 to 5
    review = models.TextField(null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Review for {self.listing.title} by {self.user.username}'