from django.test import TestCase
from django.core.exceptions import ValidationError
# from django.urls import resolve
# from django.http import HttpRequest
# from django.template.loader import render_to_string

from games.models import Game, Player
# from games.views import home_page


  
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


  def test_doesnt_save_empty_games(self):
    player_ = Player.objects.create()
    game_ = Game(player = player_, text = "")
    with self.assertRaises(ValidationError):
      game_.save()
      game_.full_clean()

