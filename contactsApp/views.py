"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.http import HttpResponseRedirect

from .models import contactsApp
from .forms import ProfileForm

def index(request):
    return render(request, 'contactsApp/index.html', {})


def list(request):
    users = contactsApp.objects.order_by('dateCreated').all()
    context = {'users': users}
    return render(request, 'contactsApp/list.html', context)


def add(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = contactsApp(name=request.POST['name'], email=request.POST['email'])
            user.save()
            return HttpResponseRedirect('/list/')
    else:
        form = ProfileForm()
    return render(request, 'contactsApp/add.html', {'form': form})