from django.db.models import indexes
from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),
    path('search/', views.profile, name= 'profile')

]
