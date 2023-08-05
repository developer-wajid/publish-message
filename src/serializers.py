from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import *

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = messages
        fields = '__all__'





class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehicles
        fields = (
            "id",
            "vehicle_no",
            "display_ip",
            "ssid",
            "password"
        )

    def validate_vehicle_no(self, value):
        """
        Check if the vehicle number is unique.
        """
        if vehicles.objects.filter(vehicle_no=value).exists():
            raise serializers.ValidationError("Vehicle number already registered.")
            # value  =  "Vehicle number already registered."
        return value
    
class UpdateVehicle(serializers.ModelSerializer):
    class Meta:
        model = vehicles
        fields = (
            "vehicle_no",
            "display_ip",
            "ssid",
            "password"
        )

    


class PublishMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = publish_message
        fields = [
            "id",
            "messages",
            "vehicles"
        ]
