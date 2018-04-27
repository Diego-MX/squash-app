from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.utils.html import escape
<<<<<<< HEAD:games/tests/test_views.py

# from django.template.loader import render_to_string

=======
# from django.template.loader import render_to_string

from games.views import home_page
from games.forms import GameForm, EMPTY_GAME_ERROR
>>>>>>> tmp:games/tests/test_views.py
from games.models import Game, Player
from games.views import home_page


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

<<<<<<< HEAD:games/tests/test_views.py
=======

  def test_home_page_uses_game_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], GameForm)  
  

>>>>>>> tmp:games/tests/test_views.py
class PlayerViewTest(TestCase):
  
  def test_uses_players_template(self):
    player_ = Player.objects.create(name="playee")
    response = self.client.get(f"/players/{player_.id}/")
    self.assertTemplateUsed(response, "player.html")
  
<<<<<<< HEAD:games/tests/test_views.py
  
  def test_passes_correct_player_to_template(self):
    other_player = Player.objects.create()
    this_player = Player.objects.create()
    response = self.client.get(f"/players/{this_player.id}/")
    self.assertEqual(response.context["player"], this_player)


  # In Book there is TEST_DISPLAYS_ONLY_ITEMS_FOR_THAT_LIST. 
  # Looks like a tricky name change. 
  def test_displays_only_games_for_that_player(self):
=======
  def test_displays_games_for_player_only(self):
>>>>>>> tmp:games/tests/test_views.py
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


  def test_saves_POST_to_existing_player(self):
    other_player = Player.objects.create()
    this_player  = Player.objects.create()

    self.client.post(f"/players/{this_player.id}/", 
        data={"game_text": "new game for this player"} )
      
    self.assertEqual(Game.objects.count(), 1)
    new_game = Game.objects.first()
    self.assertEqual(new_game.text, "new game for this player")
    self.assertEqual(new_game.player, this_player)


  def test_POST_redirects_to_player_view(self):
    other_player = Player.objects.create()
    this_player  = Player.objects.create()

    response = self.client.post(f"/players/{this_player.id}/",
        data={"game_text": "new game for this player"} )

    self.assertRedirects(response, f"/players/{this_player.id}/")


<<<<<<< HEAD:games/tests/test_views.py

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

  def test_validation_errors_sent_back_to_homepage(self):
    response = self.client.post("/players/new", data={"game_text": ""})
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, "home.html")
    expected_error = escape("You can't have an empty game.")
    self.assertContains(response, expected_error)

  def test_invalid_games_arent_saved(self):
    self.client.post("/players/new", data={"game_text": ""})
    self.assertEqual(Player.objects.count(), 0)
=======
  def test_saves_POST_to_existing_player(self):
    other_player = Player.objects.create()
    a_player = Player.objects.create()

    self.client.post(f"/players/{a_player.id}/", 
        data={"text": "new game for this player"} )
      
    self.assertEqual(Game.objects.count(), 1)
    new_game = Game.objects.first()
    self.assertEqual(new_game.text, "new game for this player")
    self.assertEqual(new_game.player, a_player)

  def test_POST_redirects_to_player_view(self):
    other_player = Player.objects.create()
    a_player     = Player.objects.create()
    response = self.client.post(
        f"/players/{a_player.id}/", 
        data={"text": "new game for this player"} )
    self.assertRedirects(response, f"/players/{a_player.id}/")

  def test_invalid_input_renders_home_template(self):
    response = self.client.post("/players/new", data={"text": ""})
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, "home.html")

  def test_validation_errors_show_on_home_page(self):
    response = self.client.post("/players/new", data={"text": ""})
    self.assertContains(response, escape(EMPTY_GAME_ERROR))  

  def test_invalid_input_passes_form_to_template(self):
    response = self.client.post("/players/new", data={"text": ""})
    self.assertIsInstance(response.context["form"], GameForm) 

  def test_validation_errors_on_player_page(self):
    player_ = Player.objects.create()
    response = self.client.post(f'/players/{player_.id}/', data={'text': ""})
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, "player.html")
    expected_error = escape(EMPTY_GAME_ERROR)
    self.assertContains(response, expected_error)

  def test_invalid_games_for_existing_player_arent_saved(self):
    player_ = Player.objects.create()
    self.client.post(f'/players/{player_.id}/', 
      data={'text': 'First'})
    self.client.post(f'/players/{player_.id}/', 
      data={'text': ''})
    self.assertEqual(Game.objects.count(), 1)

  def test_displays_game_form(self):
    player_ = Player.objects.create()
    response = self.client.get(f'/players/{player_.id}/')
    self.assertIsInstance(response.context['form'], GameForm)
    self.assertContains(response, 'name="text"')



  def post_invalid_input(self):
    player_ = Player.objects.create()
    response = self.client.post(f"/players/{player_.id}/", data={"text":""})
    return response

  def test_for_invalid_input_nothing_saved_to_db(self):
    self.post_invalid_input()
>>>>>>> tmp:games/tests/test_views.py
    self.assertEqual(Game.objects.count(), 0)

  def test_for_invalid_input_renders_list_template(self):
    response = self.post_invalid_input()
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'player.html')

  def test_for_invalid_input_passes_form_to_template(self):
      response = self.post_invalid_input()
      self.assertIsInstance(response.context['form'], GameForm)

  def test_for_invalid_input_shows_error_on_page(self):
      response = self.post_invalid_input()
      self.assertContains(response, escape(EMPTY_GAME_ERROR))



class NewPlayerTest(TestCase):
  
  def test_saves_POST_request(self):
    self.client.post("/players/new", data={"text": "A new game"} )
    self.assertEqual(Game.objects.count(), 1)
    new_game = Game.objects.first()
    self.assertEqual(new_game.text, "A new game")

    # self.assertIn("A new game", response.content.decode())
    # self.assertTemplateUsed(response, "home.html")

  def test_redirects_after_POST(self):
    response = self.client.post("/players/new", 
        data={"text": "A new game"})
    new_player = Player.objects.first()
    self.assertRedirects(response, f"/players/{new_player.id}/")
