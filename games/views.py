from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError

from games.forms import GameForm, ExistingGameForm, EMPTY_GAME_ERROR
from games.models import Game, Player

# Create your views here.

def home_page(request):
  a_form = GameForm()
  response = render(request, "home.html", {"form": a_form})
  return response

def new_player(request):
  a_form = GameForm(data=request.POST)
  if a_form.is_valid():
    player = Player.objects.create()
    a_form.save(for_player = player)
    response = redirect(player)
  else:
    response = render(request, "home.html", {"form": a_form})
  return response
  

def view_player(request, player_id):
  player = Player.objects.get(id=player_id)
  if request.method != "POST":
    a_form   = ExistingGameForm(for_player=player)
    response = render(request, 'player.html', {
        'player': player, "form": a_form})
  else:
    a_form = ExistingGameForm(for_player=player, data=request.POST)
    if a_form.is_valid():
      a_form.save()
      response = redirect(player)
    else:
      response = render(request, 'player.html', {
          'player': player, "form": a_form})
  return response
 





