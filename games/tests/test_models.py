from django.test import TestCase
from django.core.exceptions import ValidationError
<<<<<<< HEAD

from games.models import Game, Player
=======
# from django.urls import resolve
# from django.http import HttpRequest
# from django.template.loader import render_to_string

from games.models import Game, Player
# from games.views import home_page

>>>>>>> tmp

  
class GameAndPlayerModelTest(TestCase):

  def test_saves_retrieves_games(self):
    player_ = Player()
    player_.save()
    
<<<<<<< HEAD
    first_game = Game()
    first_game.text = "a_score : a_player"
    first_game.player = player_
=======
    first_game = Game.objects.create(player=player_, text="a_score : a_player")
>>>>>>> tmp
    # first_game.player1 = "a_player"
    # first_game.player2 = "other_player"
    # first_game.score1  = 3
    # first_game.score2  = 1
    first_game.save()

<<<<<<< HEAD
    second_game = Game()
    second_game.text = "b_score : b_player"
    second_game.player = player_
=======
    second_game = Game(player=player_, text="b_score : b_player")
>>>>>>> tmp
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

<<<<<<< HEAD

  def test_cannot_save_empty_game(self):
    a_player = Player.objects.create()
    a_game = Game.objects.create(text="", player=a_player)
    with self.assertRaises(ValidationError):
      a_game.save()
      a_game.full_clean()
=======
  def test_list_ordering(self):
    player_ = Player.objects.create()
    game1 = Game.objects.create(player=player_, text="a_score : a_player")
    game2 = Game.objects.create(player=player_, text="b_score : b_player")
    game3 = Game.objects.create(player=player_, text="c_score : c_player")
    self.assertEqual( list(Game.objects.all()), [game1, game2, game3] )


  def test_string_representation(self):
    game = Game(text="a_score : a_player")
    self.assertEqual(str(game), "a_score : a_player")

  def test_doesnt_save_empty_games(self):
    player_ = Player.objects.create()
    game_ = Game(player = player_, text = "")
    with self.assertRaises(ValidationError):
      game_.save()
      game_.full_clean()


  def test_get_absolute_url(self):
    player_ = Player.objects.create()
    self.assertEqual(player_.get_absolute_url(), f"/players/{player_.id}/")


  def test_invalid_duplicate_games(self):
    player_ = Player.objects.create()
    Game.objects.create(player=player_, text="score: other_player")
    with self.assertRaises(ValidationError):
      game = Game.objects.create(player=player_, text="score: other_player")
      game.full_clean()

  
  def test_saves_same_game_with_different_players(self):
    player1 = Player.objects.create()
    Game.objects.create(player=player1, text="score: other_player")
    player2 = Player.objects.create()
    game2 = Game.objects.create(player=player2, text="score: other_player")
    game2.full_clean()  # Should not raise.
>>>>>>> tmp
