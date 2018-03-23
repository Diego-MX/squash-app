from django.shortcuts import render, redirect
from django.http import HttpResponse

from games.models import Game

# Create your views here.

def home_page(request):
  response = render(request, "home.html")
  return response

 
def new_player(request):
  Game.objects.create(text=request.POST["game_text"])
  response = redirect("/players/first-player/")
  return response
  
  
def view_player(request):
  # Funciona pero es copy-paste.
  games = Game.objects.all()
  response = render(request, "player.html", {"games": games})
  return response


