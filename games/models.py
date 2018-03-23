from django.db import models

# Create your models here.
class Player(models.Model):
  objects = models.Manager()
  name    = models.TextField(default="")
  
  
class Game(models.Model):
  objects = models.Manager()
  player = models.ForeignKey(Player, default=None)
  text   = models.TextField(default="")
  # player1 = models.TextField(default="Player1")
  # player2 = models.TextField(default="Player2")
  # score1  = models.IntegerField(default=0)
  # score2  = models.IntegerField(default=0)
  


