# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

class Azienda(models.Model):

    class Meta(object):
        verbose_name = "Azienda"
        verbose_name_plural = "Aziende"
    
    ragione_sociale = models.CharField(max_length=64, unique=True)
    utente = models.OneToOneField(User)
    indirizzo = models.CharField(max_length=256)
    citta = models.CharField(max_length=256)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    logo = models.ImageField(upload_to='uploads/aziende/', blank=True, null=True)
    telefono = models.CharField(max_length=64, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    sito = models.URLField(blank=True, null=True)
    url_facebook = models.URLField(blank=True, null=True)
    partita_iva = models.CharField(max_length=64)
    data_creazione = models.DateTimeField(auto_now_add=True)
    ultima_modifica = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('azienda', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.ragione_sociale

class Caratteristica(models.Model):

    class Meta(object):
        verbose_name = "Caratteristica"
        verbose_name_plural = "Caratteristiche"

    nome = models.CharField(max_length=128, unique=True)
    data_creazione = models.DateTimeField(auto_now_add=True)
    ultima_modifica = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nome


class Tipologia(models.Model):

    class Meta(object):
        verbose_name = "Tipologia"
        verbose_name_plural = "Tipologie"

    nome = models.CharField(max_length=128, unique=True)
    descrizione = models.TextField()
    immagine = models.ImageField(upload_to='uploads/tipologie/', blank=True, null=True)
    data_creazione = models.DateTimeField(auto_now_add=True)
    ultima_modifica = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nome


class Prodotto(models.Model):

    class Meta(object):
        verbose_name = "Prodotto"
        verbose_name_plural = "Prodotti"
    
    nome = models.CharField(max_length=64, unique=True)
    azienda = models.ForeignKey(Azienda)
    tipologia = models.ForeignKey(Tipologia)
    ingombro = models.CharField(max_length=64, verbose_name=u"Dimensione", null=True, blank=True)
    efficienza = models.IntegerField(help_text=u'percentuale', blank=True, null=True)
    potenza = models.IntegerField(help_text=u'in Watt')
    costo = models.DecimalField(max_digits=9, decimal_places=2, help_text=u'in Euro €', null=True, blank=True)
    ciclo_vita = models.IntegerField(help_text=u'Durata di vita del prodotto in mesi', null=True, blank=True) # mesi
    immagine = models.ImageField(upload_to='uploads/prodotti/', blank=True, null=True)
    caratteristiche = models.ManyToManyField(Caratteristica)
    data_creazione = models.DateTimeField(auto_now_add=True)
    ultima_modifica = models.DateTimeField(auto_now=True)

    def ritorno_investimento(self):
        pass

    def __unicode__(self):
        return self.nome


class Cliente(models.Model):

    class Meta(object):
        verbose_name = "Cliente"
        verbose_name_plural = "Clienti"
    
    ragione_sociale = models.CharField(max_length=64, blank=True, null=True)
    tipo = models.CharField(max_length=64, choices=(('PRIVATO', 'Privato'), ('AZIENDA', 'Azienda')))
    codice_fiscale = models.CharField(max_length=64, help_text=u'Se è un privato')
    partita_iva = models.CharField(max_length=64, help_text=u'Se è una azienda')
    utente = models.OneToOneField(User)
    indirizzo = models.CharField(max_length=256)
    citta = models.CharField(max_length=256)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    fabbisogno_energetico = models.IntegerField(help_text=u'KWh per mq per anno')
    data_creazione = models.DateTimeField(auto_now_add=True)
    ultima_modifica = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        if self.ragione_sociale:
            return self.ragione_sociale
        else:
            return self.utente.first_name + ' ' + self.utente.last_name


class Impianto(models.Model):

    class Meta(object):
        verbose_name = "Impianto"
        verbose_name_plural = "Impianti"
    
    cliente = models.ForeignKey(Cliente, null=True, blank=True)
    prodotto = models.ForeignKey(Prodotto)
    indirizzo = models.CharField(max_length=256, null=True, blank=True)
    citta = models.CharField(max_length=256)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    nome_installazione = models.CharField(max_length=256, blank=True, null=True, help_text=u"Eventuale nome dell'impianto installato")
    data_installazione = models.DateField(blank=True, null=True)
    resa_specifica = models.CharField(max_length=256, help_text=u'KWp (KW picco)')
    immagine = models.ImageField(upload_to='uploads/impianti/', blank=True, null=True)
    pubblicato = models.BooleanField(default=True)
    data_creazione = models.DateTimeField(auto_now_add=True)
    ultima_modifica = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        if self.nome_installazione:
            return self.nome_installazione
        else:
            return self.prodotto.nome +  ' - ' + self.citta
