from django.urls import path

from . import views

app_name = 'greSiteApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('signUp', views.thanks, name='thanks'),
    ]