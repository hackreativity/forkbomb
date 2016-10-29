# -*- coding: utf-8 -*-

from django import forms

from sito.models import *

from django.contrib.auth.models import User

class AziendaForm(forms.ModelForm):

    class Meta:

        model = Azienda
        fields = [
            'ragione_sociale', 
            'email', 
            'password',
            'password2',
            'indirizzo', 
            'citta', 
            'logo', 
            'telefono', 
            'sito', 
            'url_facebook', 
            'partita_iva', 
        ]

    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Ripeti la password")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists() or Azienda.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Questa email è già registrata"
            )
        return email

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password != password2:
            print password, password2
            raise forms.ValidationError(
                "Le password non corrispondono"
            )
        return password