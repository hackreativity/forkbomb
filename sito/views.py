# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from sito.models import *

def index(request):
    return render(request, 'index.html', {})

class AziendaCreate(CreateView):
    model = Azienda


class AziendaUpdate(UpdateView):
    model = Azienda
    fields = ['name']
