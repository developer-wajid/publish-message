from django.contrib import admin
from django.urls import path 

from src.account import (   UserLoginView , 
                            home_api , 
                            VehicleAddAPIView ,
                            PublishMessageView ,
                            update_vehicle , 
                            delete_vehicle
                            )


urlpatterns = [
    #API'S
    path('user-login/',UserLoginView.as_view() ),
    path('home-api/' , home_api) ,

    path('add-vehicle/', VehicleAddAPIView.as_view(), name='add-vehicle'),
    path('update-vehicle/<int:pk>/',update_vehicle, name='update-vehicle'),
    path('delete-vehicle/',delete_vehicle, name='delete-vehicle'),
    path('publish-messages/', PublishMessageView.as_view(), name='publish-message-list'),
]
