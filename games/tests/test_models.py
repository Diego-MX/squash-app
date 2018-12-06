from django.test import TestCase
from django.core.exceptions import ValidationError
# from django.urls import resolve
# from django.http import HttpRequest
# from django.template.loader import render_to_string

from games.models import Game, Player
# from games.views import home_page


  
class GameModelTest(TestCase):

  def test_saves_retrieves_games(self):
    a_player = Player()
    a_player.save()
    
<<<<<<< HEAD
    first_game = Game()
    first_game.text = "a_score : a_player"
    first_game.player = a_player
=======
    first_game = Game.objects.create(player=player_, text="a_score : a_player")
    # first_game.player1 = "a_player"
    # first_game.player2 = "other_player"
    # first_game.score1  = 3
    # first_game.score2  = 1
>>>>>>> 0bae8bca594e839392beba506fead05c1955f41c
    first_game.save()

    second_game = Game()
    second_game.text = "b_score : b_player"
    second_game.player = a_player
    second_game.save()

    saved_player = Player.objects.first()
    self.assertEqual(saved_player, a_player)

    saved_games = Game.objects.all()
    self.assertEqual(saved_games.count(), 2)

    first_saved_game  = saved_games[0]
    second_saved_game = saved_games[1]
    self.assertEqual(first_saved_game.text,  "a_score : a_player")
    self.assertEqual(second_saved_game.text, "b_score : b_player")
    self.assertEqual(first_saved_game.player, a_player)
    self.assertEqual(second_saved_game.player, a_player)


  def test_default_text(self):
    a_game = Game()
    self.assertEqual(a_game.text, '')


  def test_game_is_related_to_player(self):
    a_player = Player.objects.create()
    a_game = Game()
    a_game.player = a_player
    a_game.save()
    self.assertIn(a_game, a_player.game_set.all())

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
    a_player = Player.objects.create()
    a_game = Game(player = a_player, text = "")
    with self.assertRaises(ValidationError):
      a_game.save()
      a_game.full_clean()


  def test_invalid_duplicate_games(self):
    a_player = Player.objects.create()
    Game.objects.create(player = a_player, text = "bla")
    with self.assertRaises(ValidationError):
      game = Game(player=a_player, text="bla")
      game.full_clean()
      # game.save()
    
  def test_allows_duplicate_games_different_players(self):
    player_1 = Player.objects.create()
    player_2 = Player.objects.create()
    Game.objects.create(player = player_1, text = "bla")
    game = Game(player = player_2, text = "bla")
    game.full_clean()  # should not raise


  def test_game_ordering(self):
    player_1 = Player.objects.create()
    game_1 = Game.objects.create(player=player_1, text='i1')
    game_2 = Game.objects.create(player=player_1, text='item 2')
    game_3 = Game.objects.create(player=player_1, text='3')
    self.assertEqual(list( Game.objects.all() ), [game_1, game_2, game_3] )

  def test_string_representation(self):
    game = Game(text='some text')
    self.assertEqual(str(game), 'some text')


class PlayerModelTest(TestCase):

  def test_get_absolute_url(self):
    a_player = Player.objects.create()
    self.assertEqual(a_player.get_absolute_url(), f"/players/{a_player.id}/")










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
