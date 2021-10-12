from django.urls import path
from . views import LoginView,LogoutView,UpdateProfileView,PasswordChangeView

urlpatterns = [
    path('login/',LoginView, name='login'), 
    path('logout/',LogoutView, name='logout'), 
    path('profileupdate/',UpdateProfileView, name='updateprofile'), 
    path('changepassword/',PasswordChangeView, name='changepassword'), 
]
