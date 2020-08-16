from django.shortcuts import render

from .models import Subscribe
from .forms import SubscribeForm

# Create your views here.
def index(request):
    subscription_entry = Subscribe()
    context = {}
    context['form'] = SubscribeForm()
    if request.GET:
        subscription_entry.email = request.GET[('subscription_field')]
        subscription_entry.save()
    return render(request, "index.html", context)
