from django.test import TestCase
from django.core.exceptions import ValidationError

from games.models import Game, Player

  
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


  def test_cannot_save_empty_game(self):
    a_player = Player.objects.create()
    a_game = Game.objects.create(text="", player=a_player)
    with self.assertRaises(ValidationError):
      a_game.save()
      a_game.full_clean()
