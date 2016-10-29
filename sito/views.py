# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from sito.models import *
from sito.forms import *

def index(request):
    return render(request, 'index.html', {})

class AziendaCreate(CreateView):
    model = Azienda
    form_class = AziendaForm
    success_url = reverse_lazy('azienda')

    def form_valid(self, form):
        print form.cleaned_data
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(username=email, email=email, password=password)
        form.instance.utente = user
        return super(AziendaCreate, self).form_valid(form)

class AziendaUpdate(UpdateView):
    model = Azienda
    fields = ['name']
