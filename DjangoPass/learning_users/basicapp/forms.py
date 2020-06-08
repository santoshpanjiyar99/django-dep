from django import forms
from django.contrib.auth.models import User
from basicapp.models import UserProfileInfo


class userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields = ('username','email','password')

class UserProfile(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('protfolio','profilePic')
