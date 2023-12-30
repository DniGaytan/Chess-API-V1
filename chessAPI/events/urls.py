from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    # path('get', views.getEvents, name='getEvents'),
    path('get/<event_id>', views.getEvent, name='getEvent'),
    path('create', views.createEvent, name='createEvent'),
    path('participation/create/<event_id>', views.createParticipation, name='createParticipation')
]