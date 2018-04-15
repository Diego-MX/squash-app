from django.test import TestCase
from django.utils.html import escape

from games.forms import GameForm, EMPTY_GAME_ERROR

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