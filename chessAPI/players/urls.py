from django.urls import path
from . import views

app_name = 'players'

urlpatterns = [
    path('get', views.getPlayers, name='getPlayers'),
    path('get/<user_id>', views.getPlayer, name='getPlayer'),
    path('create', views.createPlayer, name='createPlayer'),
]