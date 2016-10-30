# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from sito.models import *
from sito.forms import *

import simplejson as json

def index(request):

    tipologie = Tipologia.objects.all()
    prodotti = Prodotto.objects.all()
    impianti_count = Impianto.objects.count()

    return render(request, 'index.html', {
        'tipologie': tipologie,
        'prodotti': prodotti,
        'impianti_count': impianti_count,
    })

class AziendaCreate(CreateView):
    model = Azienda
    form_class = AziendaForm

    def form_valid(self, form):
        print form.cleaned_data
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(username=email, email=email, password=password)
        form.instance.utente = user
        return super(AziendaCreate, self).form_valid(form)

class AziendaUpdate(UpdateView):
    form_class = AziendaForm
    model = Azienda
    success_url = reverse_lazy('azienda')

class AziendaDetailView(DetailView):
    model = Azienda

def livemap(request):

    impianti = Impianto.objects.filter(pubblicato=True, lat__isnull=False, lon__isnull=False)
    impianti_json = json.dumps(
        list(impianti.values('id', 'cliente', 'prodotto__nome', 'indirizzo', 'citta', 'lat', 'lon', 'resa_specifica', 'immagine', 'prodotto__tipologia__nome'))
    )
    tipologie = Tipologia.objects.all()

    potenza_totale = 0
    for i in impianti:
        potenza_totale += float(i.resa_specifica)
    potenza_totale = int(potenza_totale)
    potenza_totale = "{:,}".format(potenza_totale)

    return render(request, 'livemap.html', {
        'impianti': impianti,
        'impianti_json': impianti_json,
        'tipologie': tipologie,
        'potenza_totale': potenza_totale,
    })


def underconstruction(request):
    return render(request, 'login.html', {})
