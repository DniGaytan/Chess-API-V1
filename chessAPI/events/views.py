from django.shortcuts import render
from .models import Event, EventPlayers
from players.models import Player
from matches.models import Match
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseBadRequest
import datetime

# Create your views here.

def getEvent(request, event_id):
    participations = None
    try:
        event = Event.objects.get(pk=event_id)

        participations = EventPlayers.objects.filter(event=event).select_related('player').values(
            'event_score', 'total_wins', 'total_loses', 'total_ties', 'player__user', 'player__username')
        
        matches = Match.objects.filter(event=event).select_related('player').values(
            'whites_player__user__first_name', 'whites_player__user__last_name', 'blacks_player__user__first_name', 'blacks_player__user__last_name', 'date', 'result', 'id'
        )

        print(matches)
    except Exception as e:
        print(e)
        return JsonResponse({
            "error": "Some weird shit happened"
        })
    
    json_participations = []
    if participations is not None:
        json_participations = [
            {
                'username': participation['player__username'],
                'event_score': participation['event_score'],
                'total_wins': participation['total_wins'],
                'total_loses': participation['total_loses'],
                'total_ties': participation['total_ties'],
            } for participation in participations
        ]

    json_matches = []
    if matches is not None:
        json_matches = [
            {
                'id': match['id'],
                'whites_player': match['whites_player__user__first_name'] + ' ' + match['whites_player__user__last_name'],
                'black_player': match['blacks_player__user__first_name'] + ' ' + match['blacks_player__user__last_name'],
                'result': match['result'],
                'date': match['date']
            } for match in matches
        ]


    return JsonResponse({
        'id': event.id,
        'name': event.name,
        'description': event.description,
        'type': event.event_type,
        'participations': json_participations,
        'matches': json_matches
    })

def createEvent(request):
    if request.method != 'POST':
        raise HttpResponseBadRequest

    try:
        data = request.POST
        event = Event.objects.create(
            name=data['name'],
            description=data['description'],
            is_active=True,
            event_type=data['event_type']
        )
    except Exception as e:
        pass

    return JsonResponse({
        'id': event.id,
        'name': event.name,
        'description': event.description,
        'type': event.event_type,
    })

def createParticipation(request, event_id):
    if request.method != 'POST':
        raise HttpResponseBadRequest
    
    player_id = request.POST.get('player_id', '')
    data = request.POST

    try:
        event = Event.objects.get(pk=event_id)
        user = User.objects.get(pk=player_id)
        player = Player.objects.get(user=user)

        participation = EventPlayers.objects.create(
            player = player,
            event = event,
            event_score = 0,
            total_wins = 0,
            total_loses = 0,
            total_ties = 0,
        )

    except Exception as e:
        pass

    return JsonResponse(
        {
            'participation_created': True
        }
    )



