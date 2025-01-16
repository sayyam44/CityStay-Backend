from django import forms
from .models import Poi
from django.contrib.gis.geos import Point
#This is because in models of Poi just contains the location column
# but it does not have the latitude and longitude column , but since
# actually the poi is defined using Latitude and Longitude 
# So here we are getting the data from the frontend in form of latitude,
# longitude format then we are storing it in an array named as Location


#This form is for frontend that what fields of data is being received.
class PoisForm(forms.ModelForm):
    class Meta:
        model=Poi
        fields = [
        'name',
        'type',
        'location',
        'latitude',
        'longitude',]

    latitude = forms.FloatField()
    longitude = forms.FloatField()

    #from frontend we are not getting the location field directly instead
    #we will get the latitude and longitude of the location but in the 
    # backend models.py we are not storing the latidute and longitude so we 
    # need to convert this latitude and longitude into location field. 
    def clean(self):
        data = super().clean() #form validation and data holds all the values
        #specified in the fields in this form above
        latitude = data.pop('latitude')#Retrieves and removes the latitude value from data.
        longitude = data.pop('longitude') #Retrieves and removes the longitude value from data.
        data['location'] = Point(latitude, longitude, srid=4326) 
        #Combines the latitude and longitude into a Point object.
        #srid=4326 specifies the spatial reference system (WGS 84, commonly used for latitude/longitude).
        return data

    #this is to show the the latitude and longitude field values in the 
    #listings table in localhost admin panel 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        location = self.initial.get('location')
        if isinstance(location, Point):
            self.initial['latitude'] = location.tuple[0]
            self.initial['longitude'] = location.tuple[1]