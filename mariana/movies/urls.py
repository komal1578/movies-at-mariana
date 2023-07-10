from django.urls import path
from movies.views import index,home

app_name = 'movies'
urlpatterns = [
    path('',home,name='home'),
    path('index/', index, name='index'),
]