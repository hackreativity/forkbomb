# -*- coding: utf-8 -*-

from django.contrib import admin
from sito.models import *

@admin.register(Azienda)
class AziendaAdmin(admin.ModelAdmin):

    list_display = ('ragione_sociale', 'citta', 'email', 'sito', 'data_creazione')
    search_fields = ('ragione_sociale', 'indirizzo', 'telefono', 'email', 'sito', 'url_facebook', 'partita_iva')
    list_filter = ('citta', )

@admin.register(Caratteristica)
class CaratteristicaAdmin(admin.ModelAdmin):

    list_display = ('nome', )
    search_fields = ('nome',)

@admin.register(Tipologia)
class TipologiaAdmin(admin.ModelAdmin):

    list_display = ('nome', )
    search_fields = ('nome',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):

    list_display = ("__unicode__", "tipo", "citta", "fabbisogno_energetico", )
    search_fields = ("ragione_sociale", "tipo", "codice_fiscale", "partita_iva", "utente", "indirizzo", "citta", "fabbisogno_energetico", )
    list_filter = ('tipo', )

"ragione_sociale", "tipo", "codice_fiscale", "partita_iva", "utente", "indirizzo", "citta", "fabbisogno_energetico", 

@admin.register(Impianto)
class ImpiantoAdmin(admin.ModelAdmin):

    list_display = ('__unicode__', 'prodotto', 'citta', 'nome_installazione', 'resa_specifica' )
    search_fields = ('cliente', 'prodotto', 'indirizzo', 'citta', 'nome_installazione', 'data_installazione', 'resa_specifica', 'caratteristiche', )
