from django.shortcuts import render, redirect
from django.http import HttpResponse

from games.models import Game

# Create your views here.

def home_page(request):
  if request.method != "POST": 
    response = render(request, "home.html")
  else: 
    Game.objects.create(text=request.POST["game_text"])
    response = redirect("/players/first-player/") 
  return response

 
def view_list(request):
  # Funciona pero es copy-paste.
  games = Game.objects.all()
  response = render(request, "player.html", {"games": games})
  return response