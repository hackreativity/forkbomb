# -*- coding: utf-8 -*-

"""forkbomb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from sito.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),

    url(r'azienda/register/$', AziendaCreate.as_view(), name='azienda-create'),
    url(r'azienda/update/(?P<pk>[0-9]+)/$', AziendaUpdate.as_view(), name='azienda-update'),
    url(r'azienda/profile/(?P<pk>[0-9]+)/$', AziendaDetailView.as_view(), name='azienda'),
    url(r'livemap/?$', livemap, name="livemap" )
]
