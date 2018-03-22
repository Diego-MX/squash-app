from django.shortcuts import render, redirect
from django.http import HttpResponse

from games.models import Game

# Create your views here.
def home_page(request):

  if request.method == "POST": 
    Game.objects.create(text=request.POST["game_text"])
    return redirect("/")
  
  games = Game.objects.all()
  response = render(request, "home.html", {"games": games})
  return response

  """ Código viejo. 
  # game = Game()
  # game.text = request.POST.get("game_text", "")
  # game.save()

  # if request.method == "POST":
  #   new_game_text = request.POST["game_text"]
  #   Game.objects.create(text=new_game_text)
  # else:
  #   new_game_text = ""
  # response = render(request, "home.html", 
  #     {"new_game_text": new_game_text} )

  # if request.method == "POST":
  #   response = HttpResponse(request.POST["game_text"])
  # else: 
  #   response = render(request, "home.html"

  # response = HttpResponse("") 
  """
  

  