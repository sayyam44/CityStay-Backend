from django.contrib import admin
from django.urls import path,include
from listings.api import views as listings_api_views
from users.api import views as users_api_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #here used .as_view() because in api->views.py I have made class based views
    # for listing the list of accomodations on frontend
    path('api/listings/',listings_api_views.ListingList.as_view()),

    # for creating a new listing from the frontend for Addproperty.js
    path('api/listings/create/',listings_api_views.ListingCreate.as_view()),
    
    # for showing the detail of each listing
    path('api/listings/<int:pk>/',listings_api_views.ListingDetail.as_view()),

    # for deleting the current listing
    path('api/listings/<int:pk>/delete/',listings_api_views.ListingDelete.as_view()),
    
    # for updating the current listing
    path('api/listings/<int:pk>/update/',listings_api_views.ListingUpdate.as_view()),

    # URL to add a review to a listing
    # path('api/listings/<int:pk>/add_review/', listings_api_views.AddReview.as_view()),
    # path('api/listings/<int:pk>/add_review/', listings_api_views.AddReview.as_view(), name='add_review'),
    path('api/listings/<int:pk>/add_review/', listings_api_views.AddReview.as_view(), name='add_review'),
    # To list the userprofiles that are created using django signals 
    # automatically as the user signs up
    path('api/profiles/',users_api_views.ProfileList.as_view()),

    # int:pk-> getting a single profile for the user with profile id as 
    # primary key as same as the seller id as we need to get the
    # profile on the basis of seller id and not profile id .
    path('api/profiles/<int:seller>/',users_api_views.ProfileDetail.as_view()),

    # this is to update the profile 
    path('api/profiles/<int:seller>/update/',users_api_views.ProfileUpdate.as_view()),
    
    # this is to get the messages of the current user
    path('api/profiles/<int:seller>/messages/',users_api_views.MessageList.as_view()),


    #below 2 urls will be accessed for user registeration or authentication
    path('api-auth-djoser/', include('djoser.urls')),
    path('api-auth-djoser/', include('djoser.urls.authtoken')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




