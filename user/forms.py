from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from cloudinary.forms import CloudinaryFileField


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    image = CloudinaryFileField(
        options={
            'crop': 'thumb',
            'width': 300,
            'height': 300,
            'folder': 'avatars'
        }
    )

    class Meta:
        model = Profile
        fields = ['bio', 'image']
