
from .base import FunctionalTest

from selenium.webdriver.common.keys import Keys
from unittest import skip


class ItemValidationTest(FunctionalTest):
  def test_cannot_add_empty_games(self):
    # Ana goes to the home page and accidentally tries to submit a wrong game. 

    # Home Page Refreshes and there is an error message that verified the format. 

    # She tries again with a new game text, which is correct now. 

    # Perversely, she now decides to submit a second wrong game. 

    # She gets a similar warning on the page. 

    # And she corrects it by filling ok game. 

    self.fail("Write Me!")


