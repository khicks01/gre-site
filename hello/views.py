from django.shortcuts import render

from .models import Subscribe
from .forms import SubscribeForm

# Create your views here.
def index(request):
    subscription_entry = Subscribe()
    context = {}
    context['form'] = SubscribeForm()
    if request.POST:
        subscription_entry.email = request.POST[('subscription_field')]
        subscription_entry.save()
    return render(request, "index.html", context)
