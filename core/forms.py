from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Review


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username",
                  "email", "password1", "password2"]


class ReviewForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    email = forms.EmailInput()
    review = forms.CharField(max_length=10000)

    class Meta:
        model = Review
        fields = ["username", "email", "review"]
