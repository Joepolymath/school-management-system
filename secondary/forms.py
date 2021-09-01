from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import *


class ContactForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}))
    class Meta:
        model = Contact
        fields = '__all__'
