from django.db import models
from django.contrib.auth.models import User





# user_assoisatw_with_company

class company(models.Model):
    comapany_name = models.CharField(max_length=100)

    def __str__(self):
        return self.comapany_name
    

class user_profile(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE )
    company = models.ForeignKey(company ,on_delete=models.CASCADE , related_name="comapny_users")


    def __str__(self):
        return self.user.username



class messages(models.Model):
    company     = models.ForeignKey(company ,on_delete=models.CASCADE , related_name="comapny_messages")
    message_id  = models.CharField(max_length=100)
    message     = models.TextField(max_length=500)
    status      = models.BooleanField(default=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message



class vehicles(models.Model):
    user_profile = models.ForeignKey(user_profile ,on_delete=models.CASCADE , related_name="user_vehicles" )
    vehicle_no = models.CharField(max_length=100)
    display_ip = models.CharField(max_length=100)
    ssid = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.vehicle_no
    


class publish_message(models.Model):
    user_profile = models.ForeignKey(user_profile ,on_delete=models.CASCADE , related_name="publisher" )
    messages = models.ForeignKey(messages ,on_delete=models.CASCADE , related_name="publish_message" )
    vehicles = models.ForeignKey(vehicles ,on_delete=models.CASCADE , related_name="publish_vehicle" )
    status      = models.BooleanField(default=True)


    def __str__(self):
        return self.user_profile
    

    
    
