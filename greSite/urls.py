from django.urls import path, include
from django.contrib import admin

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

admin.autodiscover()

urlpatterns = [
    path("", include('greSiteApp.urls')),
    path("admin/", admin.site.urls),
]
