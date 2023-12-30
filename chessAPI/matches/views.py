from matches.models import Match
from events.models import Event, EventPlayers
from players.models import Player
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseBadRequest
from .utils import calculateMatchResult, calculateElo
import datetime

# Create your views here.

def createMatch(request, event_id):
    if request.method != 'POST':
        raise HttpResponseBadRequest
    
    data = request.POST
    whites_player_id = data['whites_player_id']
    blacks_player_id = data['blacks_player_id']

    try:
        event = Event.objects.get(pk=event_id)
        whites_user = User.objects.get(pk=whites_player_id)
        blacks_user = User.objects.get(pk=blacks_player_id)
        whites_player = Player.objects.get(user=whites_user)
        blacks_player = Player.objects.get(user=blacks_user)

        # If users are not enrolled in event, registered them!
        # works as a failsafe, but this is not the intended sequence!

        for player in [whites_player, blacks_player]:
            EventPlayers.objects.get_or_create(
                player = player,
                event = event,
                event_score = 0,
                total_wins = 0,
                total_loses = 0,
                total_ties = 0,
            )


        match, _ = Match.objects.create(
            event = event,
            whites_player = whites_player,
            blacks_player = blacks_player,
            date = data['datetime'],
            result = 'upcoming'
        )
    except Exception as e:
        print(e)
        pass

    return JsonResponse({
        'match_id': match.id,
        'event_name': event.name,
        'whites_player': whites_user.get_full_name(),
        'blacks_player': blacks_user.get_full_name(),
        'date': data['datetime'],
        'result': match.result,
    })

def createMatchBulk(request, event_id):

    try:
        event = Event.objects.get(pk=event_id)
        participations = EventPlayers.objects.filter(event=event)
    except Exception as e:
        pass

    for participant in participations:
        for rival in participations:
            if rival is participant:
                continue
            Match.objects.create(
                event = event,
                whites_player = participant.player,
                blacks_player = rival.player,
                date = datetime.datetime.now()
            )

    return JsonResponse({
        'process_finished': True
    })

def updateMatchResult(request, match_id):
    try:
        match = Match.objects.get(id=match_id)
        match.result = request.POST['result']
        match.save()

        whites_player = Player.objects.get(user = match.whites_player)
        blacks_player = Player.objects.get(user = match.blacks_player)

        # Update individual results and ELO
        calculateMatchResult(match.event, match.whites_player, match.blacks_player, match.result)
        whites_elo, blacks_elo = calculateElo(match.whites_player, match.blacks_player, match.result)

        print(whites_elo, blacks_elo)

        whites_player.elo_score = whites_elo
        blacks_player.elo_score = blacks_elo
        whites_player.save()
        blacks_player.save()

        
    except Exception as e:
        print(e)
        pass

    return JsonResponse({
        'id': match.id,
        'whites_player': match.whites_player.username,
        'blacks_player': match.blacks_player.username,
        'date': match.date,
        'result': match.result
    })
