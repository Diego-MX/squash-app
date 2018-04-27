
from .base import FunctionalTest

from selenium.webdriver.common.keys import Keys
from unittest import skip


class GameValidationTest(FunctionalTest):
  def test_cannot_add_empty_games(self):
    # Ana goes to the home page and accidentally tries to submit a wrong game. 
    self.browser.get(self.live_server_url)
    self.get_game_input_box().send_keys(Keys.ENTER)

    # The browser intercepts the reques, and does not load the player page. 
    self.wait_for(lambda: 
      self.browser.find_element_by_css_selector("#id_text:invalid"))

    # She types text and error disappears. 
    self.get_game_input_box().send_keys("11-4 : Vanesa")
    self.wait_for(lambda: 
      self.browser.find_element_by_css_selector("#id_text:valid"))

    # And submits it successfully
    self.get_game_input_box().send_keys(Keys.ENTER)
    self.wait_for(lambda: 
      self.check_for_row_in_game_table("1: 11-4 : Vanesa") )

    # Perversely, she now decides to submit a second wrong game
    # Broser doesn't comply.
    self.get_game_input_box().send_keys(Keys.ENTER)
    self.wait_for(lambda: 
      self.browser.find_element_by_css_selector("#id_text:invalid"))

    # And she corrects it by filling ok game. 
    self.get_game_input_box().send_keys("2-11 : Diego")
    self.wait_for(lambda: 
      self.browser.find_element_by_css_selector("#id_text:valid"))
    self.get_game_input_box().send_keys(Keys.ENTER)
    self.wait_for(lambda: 
      self.check_for_row_in_game_table("1: 11-4 : Vanesa") )
    self.wait_for(lambda: 
      self.check_for_row_in_game_table("2: 2-11 : Diego") )


  def test_cannot_add_duplicate_games(self):
    # Ana empieza una lista de juegos. 
    self.browser.get(self.live_server_url)
    self.get_game_input_box().send_keys("5-11 : Valentina")
    self.get_game_input_box().send_keys(Keys.ENTER)
    self.wait_for(lambda:
      self.check_for_row_in_game_table('1: 5-11 : Valentina'))

    # She accidentally tries to enter a duplicate item
    self.get_game_input_box().send_keys('5-11 : Valentina')
    self.get_game_input_box().send_keys(Keys.ENTER)

    # She sees a helpful error message
    self.wait_for(lambda: self.assertEqual(
        self.browser.find_element_by_css_selector('.has-error').text,
        "You've already submitted this game."))

