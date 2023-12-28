from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import post

class registrationform(UserCreationForm):
    email=forms.EmailField(required=True)
    name=forms.CharField(required=False)

    class Meta:
        model=User
        fields=['name','username','email','password1','password2']
class postform(forms.ModelForm):
    class Meta:
        model=post
        fields=['title','des']