from django.db import models
from events.models import Event
from players.models import Player

# Create your models here.

class Match(models.Model):
    event = models.ForeignKey(Event, on_delete=models.PROTECT, default = 1)
    whites_player = models.ForeignKey(Player, on_delete=models.PROTECT, related_name='whites_player')
    blacks_player = models.ForeignKey(Player, on_delete=models.PROTECT, related_name='blacks_player')
    date = models.DateTimeField()
    
    RESULT_OPTIONS = (
        ('upcoming', 'Upcoming'),
        ('whites', 'Whites'),
        ('blacks', 'Blacks'),
        ('draw', 'Draw')
    )

    result = models.CharField(
        max_length=100,
        choices=RESULT_OPTIONS,
        default='upcoming'
    )