from django.test import TestCase
from django.utils.html import escape

from games.models import Game, Player
from games.forms  import (GameForm, ExistingGameForm, 
      EMPTY_GAME_ERROR, DUPLICATE_GAME_ERROR)


class GameFormTest(TestCase):
  
  def test_form_game_input_has_placeholder_and_css_classes(self):
    # ESCAPE changes both " <, but not both are escaped in AS_P.
    a_form = GameForm()
    self.assertIn('placeholder="Enter game &lt;SCORE : PLAYER_AGAINST&gt;"', 
        a_form.as_p())
    self.assertIn('class="form-control input-lg"', a_form.as_p())


  def test_form_validation_for_blank_games(self):
    a_form = GameForm(data={'text': ''})
    self.assertFalse(a_form.is_valid())
    self.assertEqual(a_form.errors['text'], [EMPTY_GAME_ERROR])


  def test_form_save_handles_saving_to_player(self):
    a_player = Player.objects.create()
    a_form   = GameForm(data={'text': 'A new game'})
    new_game = a_form.save(for_player=a_player)  
    self.assertEqual(new_game, Game.objects.first())
    self.assertEqual(new_game.text, "A new game")
    self.assertEqual(new_game.player, a_player)



class ExistingGameFormTest(TestCase):

  def test_form_renders_game_text_input(self):
    a_player = Player.objects.create()
    form = ExistingGameForm(for_player=a_player)
    self.assertIn('placeholder="Enter game &lt;SCORE : PLAYER_AGAINST&gt;"', 
        form.as_p())

  def test_form_validation_for_blank_games(self):
    a_player = Player.objects.create()
    form = ExistingGameForm(for_player=a_player, data={'text': ''})
    self.assertFalse(form.is_valid())
    self.assertEqual(form.errors['text'], [EMPTY_GAME_ERROR])

  def test_form_validation_for_duplicate_games(self):
    a_player = Player.objects.create()
    Game.objects.create(player=a_player, text='no twins!')
    form = ExistingGameForm(for_player=a_player, data={'text': 'no twins!'})
    self.assertFalse(form.is_valid())
    self.assertEqual(form.errors['text'], [DUPLICATE_GAME_ERROR])

  def test_form_save(self):
    a_player = Player.objects.create()
    a_form   = ExistingGameForm(for_player=a_player, data={'text': 'hi'})
    new_game = a_form.save()
    self.assertEqual(new_game, Game.objects.all()[0])


