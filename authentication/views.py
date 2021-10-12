from django.shortcuts import render,redirect
from django.contrib.auth import (authenticate, login, logout, get_user_model, update_session_auth_hash)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from .forms import UserLoginForm ,UserUpdateForm,UserProfileUpdate
from .models import UserProfile

def LoginView(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user_name = form.cleaned_data.get('user_name')
        password = form.cleaned_data.get('password')
        user = authenticate(user_name=user_name, password=password)
        #login the user
        login(request, user)
        #pass the message
        messages.success(request,"Login is Successful!!")
        if next:
            return redirect(next)
        return redirect('home')
    return render(request,'login.html',{"form":form})

#logout the user and
def LogoutView(request):
    logout(request)
    messages.success(request,"Log out Successful!!")
    return redirect('login')


#Update the profile

@login_required(login_url='login/')
def UpdateProfileView(request):
    if request.method == 'POST':
        user_update = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileUpdate(request.POST, request.FILES,instance=request.userprofile)
        #check the validity of the two forms:
        if user_update.is_valid() and profile_form.is_valid() :
            user_update.save()
            profile_form.save()
            #pass the messages
            messages.success(request,'Profile Updated Successfully')
            
        else:
            messages.error(request,'Error Updating Your Profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profle_form = UserProfileUpdate(instance=request.user.userprofile)
        
    context = {
         'user':request.user,
        'user_form':user_form,
        'profile_form':profle_form
    }
    return render(request,'dashboard/profile.html',context)
#password reset
@login_required(login_url='login/')
def PasswordChangeView(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"Password successfully updated. Please Login again")
            return redirect('login')
        else:
            messages.error(request,"Error Changing the password. Please Try again")
    else:
        form = PasswordChangeForm(request.user)
    context ={
        'form':form,
        'user':request.user,
    }
    return render(request,'dashboard/change_password.html',context)

#
# def home(request):
#     if request.user.is_authenticated:
#         return redirect('/account/dashboard')
#     else:
#         return redirect('/account/login')


# @login_required(login_url='/account/login/')
# def dashboard(request):
#     pro_count = Property.objects.filter(user=request.user).count()
#     context = {
#         'user':request.user,
#         'pro_count':pro_count
#     }
#     return render(request,'dashboard/dashboard.html',context)

# @login_required(login_url='/account/login/')
# def all_notifications(request):
#     unread_notifications = Notification.objects.filter(to_user=request.user, is_read=False)
#     read_notifications = Notification.objects.filter(to_user=request.user, is_read=True)
#     count = len(unread_notifications)
#     context={
#         'unread_notifications':unread_notifications,
#         'read_notifications': read_notifications,
#         'count': count,
#         'user':request.user
#     }
#     return render(request,'dashboard/notifications.html',context)
# def mark_all_as_read(request):
#    unread_notifications = Notification.objects.filter(to_user=request.user,is_read=False)
#    for obj in unread_notifications:
#        obj.is_read = True
#        obj.save()

#    return redirect('/account/dashboard/notifications')
# def mark_one_as_read(request,id=None):
#       notification = get_object_or_404(Notification,id = id)
#       notification.is_read = True
#       notification.save()
#       return redirect('/account/dashboard/notifications')

# @login_required(login_url='/account/login/')
# def newsupdates(request):
#     return render(request,'dashboard/news&updates.html',{})

# @login_required(login_url='/account/login/')
# def billing(request):
#     return render(request,'dashboard/billing.html',{})

        
