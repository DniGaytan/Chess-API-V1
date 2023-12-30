from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('get', views.getUsers, name='getUsers'),
    path('get/<user_id>', views.getUser, name='getUser'),
    path('create', views.createUser, name='createUser'),
]