from events.models import EventPlayers
from players.models import Player

def calculateMatchResult(event, whites_player, blacks_player, result):
    participation = EventPlayers.objects.get(event=event, player=whites_player)
    participation.event_score += 3 if result == 'whites' else (1 if result == 'draw' else 0)
    participation.total_wins += 1 if result == 'whites' else 0
    participation.total_loses += 1 if result == 'blacks' else 0
    participation.total_ties += 1 if result == 'draw' else 0
    participation.save()

    participation = EventPlayers.objects.get(event=event, player=blacks_player)
    participation.event_score += 3 if result == 'blacks' else (1 if result == 'draw' else 0)
    participation.total_wins += 1 if result == 'blacks' else 0
    participation.total_loses += 1 if result == 'whites' else 0
    participation.total_ties += 1 if result == 'draw' else 0
    participation.save()

    return True

def calculateElo(whites_player, blacks_player, result):
    k = 20

    whites_player_elo = whites_player.elo_score
    blacks_player_elo = blacks_player.elo_score
    # calculates winning prob for Whites player
    wp = calculateProbability(blacks_player_elo, whites_player_elo)
    print('WP', wp)
    # calculates winning prob for Blacks player
    bp = calculateProbability(whites_player_elo, blacks_player_elo)
    print('BP', bp)

    print(result)

    if(result == 'whites'):
        whites_player_elo = whites_player_elo + k * (1 - wp)
        print(whites_player_elo)
        blacks_player_elo = blacks_player_elo + k * (0 - bp)
        print(whites_player_elo)
    elif(result == 'blacks'):
        whites_player_elo = whites_player_elo + k * (0 - wp)
        blacks_player_elo = blacks_player_elo + k * (1 - bp)

    # PENDING: What happens when there is a tie?

    return [whites_player_elo, blacks_player_elo]

def calculateProbability(whites_rating, blacks_rating):
    return 1.0 * 1.0 / (1 + 1.0 * 10**(1.0*(whites_rating-blacks_rating) / 400));

