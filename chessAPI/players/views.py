from django.contrib.auth.models import User
from .models import Player
from django.http import JsonResponse, HttpResponseBadRequest
from django.core import serializers
import json
import datetime

# Create your views here.
def getPlayers(request):
    if request.method != 'GET':
        raise HttpResponseBadRequest
    
    try:
        players = Player.objects.filter().select_related('user').values('username', 'elo_score', 'user__first_name', 'user__last_name', 'user__email', 'user__id')
    except Exception as e:
        print(e)
        return JsonResponse({
            'error': 'Some weird shit happened'
        })
    
    players = [
        {
            'id': player['user__id'],
            'username': player['username'],
            'first_name': player['user__first_name'],
            'last_name': player['user__last_name'],
            'email': player['user__email'],
            'elo_score': player['elo_score']
        } for player in players
    ]

    return JsonResponse(players, safe = False)

def getPlayer(request, user_id):
    if request.method != 'GET':
        raise HttpResponseBadRequest
    
    try:
        user = User.objects.get(pk=user_id)
        player = Player.objects.get(user=user)
    except Exception as e:
        return JsonResponse({
            'error': 'Some weird shit happened'
        })
    
    return JsonResponse({
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "username": player.username,
        "elo_score": player.elo_score
    })

def createPlayer(request):

    if request.method != "POST":
        return HttpResponseBadRequest

    data = request.POST

    try:
        user = User.objects.get(pk=data['user_id'])

        player, _ = Player.objects.get_or_create(
            user=user,
            username=data['username'],
            elo_score=data['elo_score'],
        )

    except Exception as e:
        pass

    user = User.objects.get(pk=data['user_id'])
    player = Player.objects.get(pk=player.user)

    return JsonResponse({
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "username": player.username,
        "elo_score": player.elo_score
    })