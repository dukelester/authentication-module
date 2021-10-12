from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
#creating the models for user accounts:

def upload_location(instance, filename):
    return "%s/avatar/%s" % (instance.user, filename)


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    user_name = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=12)
    email_address = models.EmailField()
    about_user = models.TextField()
    country_name = models.CharField(max_length=60)
    city_name = models.CharField(max_length=60)
    address_1 = models.CharField(max_length=60)
    address_2 = models.CharField(max_length=60)
    avator = models.ImageField(upload_to=upload_location)
    
    def __str__(self):
        return self.user_name
    
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "Users Profiles"
        
#define a signal to create the user profile automatically

def createProfile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.create(user=kwargs['instance'])

post_save.connect(createProfile, sender=User)
    
        
        