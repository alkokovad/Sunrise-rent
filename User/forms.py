from django.contrib.auth.forms import UserCreationForm

from .models import User
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'phone_number')


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']
