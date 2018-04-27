from django.test import TestCase
from django.utils.html import escape

from games.forms import GameForm, EMPTY_GAME_ERROR
from games.models import Player, Game


class GameFormTest(TestCase):
  
  def test_form_game_input_has_placeholder_and_css_classes(self):
    form_ = GameForm()
    # ESCAPE changes both " <, but not both are escaped in AS_P.
    self.assertIn(
      'placeholder="Enter game &lt;SCORE : PLAYER_AGAINST&gt;"', 
      form_.as_p())
    self.assertIn('class="form-control input-lg"', form_.as_p())


  def test_form_validation_for_blank_games(self):
    form_ = GameForm(data={'text': ''})
    self.assertFalse(form_.is_valid())
    self.assertEqual(form_.errors['text'], [EMPTY_GAME_ERROR])


  def test_form_save_handles_saving_to_a_list(self):
    player_ = Player.objects.create()
    form_ = GameForm(data={'text': 'Won : Toño'})
    new_game = form_.save(for_player=player_)
    self.assertEqual(new_game, Game.objects.first())
    self.assertEqual(new_game.text, "Won : Toño")
    self.assertEqual(new_game.player, player_)
