from django.urls import path
from . import views
urlpatterns = [
    path('',views.base,name='base'),
    path('home/',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('create-post',views.createpost,name='create-post'),
    path('profile/',views.profile,name='profile')
    
]
