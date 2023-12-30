from django.db import models
from players.models import Player

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length = 1200)
    picture_url = models.URLField()
    is_active = models.BooleanField(default=True)
    is_registration_active = models.BooleanField(default=True)
    
    EVENT_TYPES = (
        ('league', 'League'),
        ('tournament', 'Tournament'),
        ('friendly', 'Friendly')
    )

    event_type = models.CharField(
        max_length=100,
        choices=EVENT_TYPES,
        default='league'
    )

class EventPlayers(models.Model):
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    event_score = models.IntegerField()
    total_wins = models.IntegerField()
    total_loses = models.IntegerField()
    total_ties = models.IntegerField()