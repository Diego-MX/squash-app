from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Player(models.Model):
  objects = models.Manager()
  name    = models.TextField(default="")

  def get_absolute_url(self):
    response = reverse("view_player", args=[self.id])  # pylint: disable=no-member 
    return response
  
class Game(models.Model):
  objects = models.Manager()
  player = models.ForeignKey(Player, default=None)
  text   = models.TextField(default="")
  # player1 = models.TextField(default="Player1")
  # player2 = models.TextField(default="Player2")
  # score1  = models.IntegerField(default=0)
  # score2  = models.IntegerField(default=0)
  


