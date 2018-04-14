
from .base import FunctionalTest

from selenium.webdriver.common.keys import Keys
from unittest import skip


class GameValidationTest(FunctionalTest):
  def test_cannot_add_empty_games(self):
    # Ana goes to the home page and accidentally tries to submit a wrong game. 
    self.browser.get(self.live_server_url)
    self.browser.find_element_by_id("id_new_game").send_keys(Keys.ENTER)

    # Home Page Refreshes and there is an error message that verified the format. 
    self.wait_for(lambda:
      self.assertEqual(
        self.browser.find_element_by_css_selector(".has-error").text,
        "You can't have an empty game." ) )

    # She tries again with a new game text, which is correct now. 
    self.browser.find_element_by_id("id_new_game").send_keys("11-3 : Andrea")
    self.browser.find_element_by_id("id_new_game").send_keys(Keys.ENTER)
    self.wait_for(lambda: 
      self.check_for_row_in_game_table("1: 11-3 : Andrea") )

    # Perversely, she now decides to submit a second wrong game. 
    self.browser.find_element_by_id("id_new_game").send_keys(Keys.ENTER)

    # She gets a similar warning on the page. 
    self.wait_for(lambda:
      self.assertEqual(
        self.browser.find_element_by_css_selector(".has-error").text,
        "You can't have an empty game."
    ))

    # And she corrects it by filling ok game. 
    self.browser.find_element_by_id("id_new_game").send_keys("2-11 : Diego")
    self.browser.find_element_by_id("id_new_game").send_keys(Keys.ENTER)
    self.wait_for(lambda: 
      self.check_for_row_in_game_table("1: 11-3 : Andrea") )
    self.wait_for(lambda: 
      self.check_for_row_in_game_table("2: 2-11 : Diego") )


