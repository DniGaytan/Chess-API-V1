from django.urls import path
from . import views

app_name = 'matches'

urlpatterns = [
    # path('get', views.getPlayers, name='getPlayers'),
    # path('get/<user_id>', views.getPlayer, name='getPlayer'),
    path('create/<event_id>', views.createMatch, name='createMatch'),
    path('create/bulk/<event_id>', views.createMatchBulk, name='createMatchBulk'),
    path('update/<match_id>', views.updateMatchResult, name='updateMatchResult')
]