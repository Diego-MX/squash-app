from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

# from django.template.loader import render_to_string

from games.views import home_page
from games.models import Game, Player


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


  # def test_only_saves_games_when_necessary(self):
  #   self.client.get("/")
  #   self.assertEqual(Game.objects.count(), 0)

  
class GameAndPlayerModelTest(TestCase):

  def test_saves_retrieves_games(self):
    player_ = Player()
    player_.save()
    
    first_game = Game()
    first_game.text = "a_score : a_player"
    first_game.player = player_
    # first_game.player1 = "a_player"
    # first_game.player2 = "other_player"
    # first_game.score1  = 3
    # first_game.score2  = 1
    first_game.save()

    second_game = Game()
    second_game.text = "b_score : b_player"
    second_game.player = player_
    # first_game.player1 = "a_player"
    # first_game.player2 = "yet_another_player"
    # first_game.score1  = 2
    # first_game.score2  = 3
    second_game.save()

    saved_player = Player.objects.first()
    self.assertEqual(saved_player, player_)

    saved_games = Game.objects.all()
    self.assertEqual(saved_games.count(), 2)

    first_saved_game  = saved_games[0]
    second_saved_game = saved_games[1]
    self.assertEqual(first_saved_game.text, "a_score : a_player")
    self.assertEqual(second_saved_game.text, "b_score : b_player")
    self.assertEqual(first_saved_game.player, player_)
    self.assertEqual(second_saved_game.player, player_)


class PlayerViewTest(TestCase):

  def test_uses_players_template(self):
    player_ = Player.objects.create(name="playee")
    response = self.client.get(f"/players/{player_.id}/")
    self.assertTemplateUsed(response, "player.html")
  
  
  def test_displays_all_games(self):
    player_1 = Player.objects.create(name="playee")
    Game.objects.create(text="gamey 1", player=player_1)
    Game.objects.create(text="gamey 2", player=player_1)
    other_player = Player.objects.create()
    Game.objects.create(text="gamey 3", player=other_player)
    Game.objects.create(text="gamey 4", player=other_player)

    response = self.client.get(f"/players/{player_1.id}/")

    self.assertContains(response, "gamey 1")
    self.assertContains(response, "gamey 2")
    self.assertNotContains(response, "gamey 3")
    self.assertNotContains(response, "gamey 4")

  def test_passes_correct_player_to_template(self):
    other_player = Player.objects.create()
    a_player = Player.objects.create()
    response = self.client.get(f"/players/{a_player.id}/")
    self.assertEqual(response.context["player"], a_player)


class NewPlayerTest(TestCase):
  
  def test_saves_POST_request(self):
    self.client.post("/players/new", data={"game_text": "A new game"} )
    self.assertEqual(Game.objects.count(), 1)
    new_game = Game.objects.first()
    self.assertEqual(new_game.text, "A new game")

    # self.assertIn("A new game", response.content.decode())
    # self.assertTemplateUsed(response, "home.html")

  def test_redirects_after_POST(self):
    response = self.client.post("/players/new", 
        data={"game_text": "A new game"})
    new_player = Player.objects.first()
    self.assertRedirects(response, f"/players/{new_player.id}/")


class NewGameTest(TestCase):

  def test_saves_POST_to_existing_player(self):
    other_player = Player.objects.create()
    a_player = Player.objects.create()

    self.client.post(f"/players/{a_player.id}/add_game", 
        data={"game_text": "new game for this player"} )
      
    self.assertEqual(Game.objects.count(), 1)
    new_game = Game.objects.first()
    self.assertEqual(new_game.text, "new game for this player")
    self.assertEqual(new_game.player, a_player)


  def test_redirects_to_player_view(self):
    other_player = Player.objects.create()
    a_player     = Player.objects.create()

    response = self.client.post(
        f"/players/{a_player.id}/add_game", 
        data={"game_text": "new game for this player"} )

    self.assertRedirects(response, f"/players/{a_player.id}/")









