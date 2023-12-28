from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
    path('',include('django.contrib.auth.urls')) # we can use the django in-built-forms
]
