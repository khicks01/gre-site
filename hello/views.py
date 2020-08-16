from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Greeting, Subscribe
from .forms import SubscribeForm

# Create your views here.
def index(request):
    subscription_entry = Subscribe()
    context = {}
    context['form'] = SubscribeForm()
    if request.POST:
        subscription_entry.email = request.POST['subscription_field']
        subscription_entry.save()
    return render(request, "index.html", context)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
