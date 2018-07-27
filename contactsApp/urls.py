from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import contactsApp.forms

import contactsApp.views
from contactsApp import views





urlpatterns = [
    # Examples:
   url(r'^$', views.index, name='index'),
    url(r'^list/', views.list, name='list'),
    url(r'^add/', views.add, name='add'),
]