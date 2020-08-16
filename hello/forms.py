from django import forms 

class SubscribeForm(forms.Form):
    subscription_field= forms.EmailField(max_length=200)