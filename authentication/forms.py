from django import forms
from django.contrib.auth import (authenticate, login, logout, get_user_model)
from django.contrib.auth.forms import PasswordChangeForm
from . models import UserProfile

User = get_user_model()

class UserLoginForm(forms.Form):
    # first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"First Name"}))
    # last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Last Name"}))
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"User Name"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Enter Your Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"Enter Password"}))
    
    def clean(self, *args, **kwargs):
        user_name = self.cleaned_data['user_name']
        password = self.cleaned_data['password']
        print(user_name, password, "user name and password")
        
        if user_name is not None and password:
            user = authenticate(user_name=user_name, password=password)
            if not user:
                raise forms.ValidationError('Please check your details and try again!!')
            else:
                if not user.check_password(password):
                    raise forms.ValidationError("Invalid Password!")
                if not user.is_active:
                    raise forms.ValidationError('This user is no longer ACtive!')
                
            return super(UserLoginForm,self).clean(*args, **kwargs)
        
#Updating the user profile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields =('first_name','last_name','email')
        
class UserProfileUpdate(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)