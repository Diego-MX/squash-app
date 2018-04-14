from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError

from games.models import Game, Player

# Create your views here.

def home_page(request):
  response = render(request, "home.html")
  return response

def new_player(request):
  player_ = Player.objects.create()
  game_ = Game.objects.create(text=request.POST["game_text"], player=player_)
  try:
    game_.full_clean()
  except ValidationError:
    player_.delete()
    error_ = "You can't have an empty game."
    return render(request, "home.html", {"error": error_}) 
  return redirect(f"/players/{player_.id}/")
  
   
def view_player(request, player_id):
  player_ = Player.objects.get(id=player_id)
  response = render(request, "player.html", {"player": player_})
  return response

def add_game(request, player_id):
  player_ = Player.objects.get(id=player_id)
  Game.objects.create(text=request.POST["game_text"], player=player_)
  response = redirect(f"/players/{player_.id}/")
  return response


