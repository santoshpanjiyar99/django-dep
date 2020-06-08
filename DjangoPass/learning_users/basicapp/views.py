from django.shortcuts import render
from basicapp.forms import userform,UserProfile
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def index(request):
    return render(request,'basicapp/index.html')
@login_required
def special(request):
    return HttpResponse("Logged In")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered=False

    if request.method =="POST":
        user_form=userform(data=request.POST)
        profile_form=UserProfile(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pics' in request.FILES:
                profile.profile_pic=request.Files['profile_pics']

            profile.save()

            registered=True
        else:
            print(user_form.errors,profile_form.errors)

    else:
         user_form=userform()
         profile_form=UserProfile()

    return render(request,'basicapp/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})
def user_login(request):

    if request.method=='POST':
      username=request.POST.get('username')
      password=request.POST.get('password')
      user=authenticate(username=username,password=password)

      if user:
        if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
        else:
          return HttpResponse("Account not active")
      else:
         return HttpResponse("invalid username and password")
    else:
        return render(request,'basicapp/login.html',{})