from django import forms
from django.core.exceptions import ValidationError
from games.models import Game

EMPTY_GAME_ERROR = "You can't have an empty game."
DUPLICATE_GAME_ERROR  = "You've saved this game already."


class GameForm(forms.models.ModelForm):
  
  class Meta:
    model   = Game
    fields  = (
      "text",
    )
    widgets = {
      'text': forms.fields.TextInput(attrs={
          'placeholder': "Enter game <SCORE : PLAYER_AGAINST>",
          'class': 'form-control input-lg', 
    }) }
    error_messages = {
<<<<<<< HEAD
        'text': {'required': EMPTY_GAME_ERROR}
    }

  def save(self, for_player):
    self.instance.player = for_player
    return super().save()


class ExistingGameForm(GameForm):
  def __init__(self, for_player, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.instance.player = for_player
  
  def validate_unique(self):
    try:
        self.instance.validate_unique()
    except ValidationError as err:
        err.error_dict = {'text': [DUPLICATE_GAME_ERROR]}
        self._update_errors(err)

  def save(self):
    the_save = forms.models.ModelForm.save(self)
    return the_save
=======
      'text': {'required': EMPTY_GAME_ERROR}
    }

  def save(self, for_player):
    self.instance.player = for_player   # pylint: disable=no-member 
    return super().save()               # pylint: disable=no-member 
>>>>>>> 0bae8bca594e839392beba506fead05c1955f41c


