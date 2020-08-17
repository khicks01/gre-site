from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

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
        return HttpResponseRedirect(reverse('greSiteApp:thanks'))
    return render(request, "index.html", context)

def thanks(request):
    return render(request, 'thanks.html')