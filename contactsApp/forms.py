"""
Definition of forms.
"""

from django import forms
from django.core.validators import validate_email

from .models import contactsApp

class ProfileForm(forms.Form):
    name = forms.CharField(label='Name*', max_length=220, widget=forms.TextInput(attrs={'placeholder':'Enter your first name'}))
    email = forms.EmailField(label='Email*', max_length=60, widget=forms.TextInput(attrs={'placeholder':'Enter a valid email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        if contactsApp.objects.filter(email=email).exists():
            raise forms.ValidationError('This email has been taken')
        return email