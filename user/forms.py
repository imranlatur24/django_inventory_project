from django import forms
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import fields
from .models import ProfileModel

class CreateUserForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        # fields="__all__"
        fields=['username','email','password1','password2']

#create form for  update profile
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=ProfileModel
        fields=['address','phone','image']