from django import forms
from games.models import Game

EMPTY_GAME_ERROR = "You can't have an empty game."


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
      'text': {'required': EMPTY_GAME_ERROR}
    }

  def save(self, for_player):
    self.instance.player = for_player   # pylint: disable=no-member 
    return super().save()               # pylint: disable=no-member 


