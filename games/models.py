from django.db import models

# Create your models here.
class Game(models.Model):
  text = models.TextField(default="")
  # player1 = models.TextField(default="Player1")
  # player2 = models.TextField(default="Player2")
  # score1  = models.IntegerField(default=0)
  # score2  = models.IntegerField(default=0)
