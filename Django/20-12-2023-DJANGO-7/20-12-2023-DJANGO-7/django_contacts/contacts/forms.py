from django import forms
from django.forms import ModelForm
from .models import Contact, User

class ContactModelForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class AdminModelForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"