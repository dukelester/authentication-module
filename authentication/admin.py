from django.contrib import admin

# Register your models here.
from . models import UserProfile

class UserAdminProfile(admin.ModelAdmin):
    list_display = ['first_name','last_name','user_name','phone_number']
    search_fields = ('user_name','phone_number')
    
    class Meta:
        model = UserProfile
    
admin.site.register(UserProfile, UserAdminProfile)
