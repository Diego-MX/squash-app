from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError

from games.forms import GameForm
from games.models import Game, Player

# Create your views here.

def home_page(request):
  response = render(request, "home.html", {"form": GameForm()})
  return response

def new_player(request):
  player_ = Player.objects.create()
  game_ = Game.objects.create(text=request.POST["game_text"], player=player_)
  try:
    game_.full_clean()
    response = redirect(player_)
  except ValidationError:
    player_.delete()
    error_ = "You can't have an empty game."
    response = render(request, "home.html", {"error": error_}) 
  return response
  
   
def view_player(request, player_id):
  player_ = Player.objects.get(id=player_id)
  if request.method != "POST":
    response = render(request, "player.html", {"player": player_})
  else:
    try:
      game_ = Game(player=player_, text=request.POST["game_text"])
      game_.full_clean()
      game_.save()
      response = redirect(player_)
    except ValidationError:
      error_ = "You can't have an empty game."
      response = render(request, "player.html", 
          {"player": player_, "error": error_})
  return response




