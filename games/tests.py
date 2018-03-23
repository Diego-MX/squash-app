from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

# from django.template.loader import render_to_string

from games.views import home_page
from games.models import Game


class HomePageTest(TestCase):

  # def test_root_url_resolve_to_home_page_view(self):
  #   found = resolve("/")
  #   self.assertEqual(found.func, home_page)

  def test_uses_home_template(self):
    response = self.client.get("/")
    self.assertTemplateUsed(response, "home.html")   
    ### request  = HttpRequest()
    # response = home_page(request)
    # html = response.content.decode("utf8")
    ### self.assertTrue(html.startswith("<html>"))
    # self.assertIn("<title>Games played</title>", html)  # Viene del Test funcional. 
    # self.assertTrue(html.strip().endswith("</html>"))
    ### expected_html = render_to_string("home.html")
    # self.assertEqual(html, expected_html) 


  # def test_displays_all_list_games(self):
  #   Game.objects.create(text="gamey 1")
  #   Game.objects.create(text="gamey 2")
  #   response = self.client.get("/")
  #   self.assertIn("gamey 1", response.content.decode())
  #   self.assertIn("gamey 2", response.content.decode())


  def test_saves_POST_request(self):
    self.client.post("/", data={"game_text": "A new game"} )
    self.assertEqual(Game.objects.count(), 1)
    new_game = Game.objects.first()
    self.assertEqual(new_game.text, "A new game")

    # self.assertIn("A new game", response.content.decode())
    # self.assertTemplateUsed(response, "home.html")

  def test_redirects_after_POST(self):
    response = self.client.post("/", 
        data={"game_text": "A new game"})
    self.assertEqual(response.status_code, 302)
    self.assertEqual(response["location"], "/players/first-player/")


  def test_only_saves_games_when_necessary(self):
    self.client.get("/")
    self.assertEqual(Game.objects.count(), 0)

  
class GameModelTest(TestCase):

  def test_saves_retrieves_games(self):
    first_game = Game()
    first_game.text = "a_score : a_player"
    # first_game.player1 = "a_player"
    # first_game.player2 = "other_player"
    # first_game.score1  = 3
    # first_game.score2  = 1
    first_game.save()

    second_game = Game()
    second_game.text = "b_score : b_player"
    # first_game.player1 = "a_player"
    # first_game.player2 = "yet_another_player"
    # first_game.score1  = 2
    # first_game.score2  = 3
    second_game.save()

    saved_games = Game.objects.all()
    self.assertEqual(saved_games.count(), 2)

    first_saved_game  = saved_games[0]
    second_saved_game = saved_games[1]
    self.assertEqual(first_saved_game.text, "a_score : a_player")
    self.assertEqual(second_saved_game.text, "b_score : b_player")


class ListViewTest(TestCase):

  def test_uses_players_template(self):
    response = self.client.get("/players/first-player/")
    self.assertTemplateUsed(response, "player.html")
  
  
  def test_displays_all_games(self):
    Game.objects.create(text="gamey 1")
    Game.objects.create(text="gamey 2")

    response = self.client.get("/players/first-player/")

    self.assertContains(response, "gamey 1")
    self.assertContains(response, "gamey 2")





