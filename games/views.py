from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
  # response = HttpResponse("")
  
  # if request.method == "POST":
  #   return HttpResponse(request.POST["game_text"])
  # return render(request, "home.html")

  response = render(request, "home.html", 
      {"new_game_text": request.POST.get("game_text", "")
  })
  return response

  