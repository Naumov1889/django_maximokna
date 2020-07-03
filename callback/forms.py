from django import forms
from .models import Callback
from django.db import models

class CallbackForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Имя',
        'class': 'input form__input',
        'id': ''
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Номер телефона',
        'class': 'input form__input',
        'id': ''
    }))
    whenToCall = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Когда вам позвонить?',
        'class': 'input form__input',
        'id': ''
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'e-mail',
        'class': 'input form__input',
        'id': ''
    }))
# TODO: get rid of popbox__input in front-end
