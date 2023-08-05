from django.contrib import admin
from .models import vehicles, publish_message, user_profile, messages,company



admin.site.site_header  =  "Shreenath Bus Admin"  
admin.site.site_title  =  "Shreenath Bus Admin"
admin.site.index_title  =  "Shreenath Bus Admin"


admin.site.register(company)





@admin.register(user_profile)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ('company', 'user')
    search_fields = ('user__username','company__company_name')



@admin.register(messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ('company', 'message_id', 'message', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = ('message_id', 'message')



@admin.register(vehicles)
class VehiclesAdmin(admin.ModelAdmin):
    list_display = ('vehicle_no', 'user_profile', 'display_ip', 'ssid')  # Fields to display in the list view
    list_filter = ('user_profile',)  # Add filters for user_profile field
    search_fields = ('vehicle_no', 'user_profile__username')  # Add search fields
    list_per_page = 20  # Number of items per page in the list view

