
from .base import FunctionalTest

from selenium.webdriver.common.keys import Keys
from unittest import skip


class ItemValidationTest(FunctionalTest):
  def test_cannot_add_empty_games(self):
    # Ana goes to the home page and accidentally tries to submit a wrong game. 
    self.browser.get(self.live_server_url)
    self.get_game_input_box().send_keys(Keys.ENTER)

    # Home Page Refreshes and there is an error message that verified the format. 
    self.wait_for(lambda: 
      self.browser.find_elements_by_css_selector('#id_text:invalid'))

    # She tries again with a new game text, which is correct now.
    # The error disappears. 
    self.get_game_input_box().send_keys("11-3 : Andrea")
    self.wait_for(lambda: 
      self.browser.find_elements_by_css_selector('#id_text:valid'))
    
    # And she can submit it successfully.
    self.get_game_input_box().send_keys(Keys.ENTER)
    self.wait_for(lambda: 
      self.check_for_row_in_game_table("1: 11-3 : Andrea") )

    # Perversely, she now decides to submit a second wrong game. 
    self.get_game_input_box().send_keys(Keys.ENTER)

    # She gets a similar warning on the page. 
    self.wait_for(lambda: 
      self.check_for_row_in_game_table("1: 11-3 : Andrea") )
    self.wait_for(lambda: 
      self.browser.find_elements_by_css_selector('#id_text:invalid'))

    # And she corrects it by filling ok game. 
    self.get_game_input_box().send_keys("2-11 : Diego")
    self.wait_for(lambda: 
      self.browser.find_elements_by_css_selector('#id_text:valid'))
    self.get_game_input_box().send_keys(Keys.ENTER)
    self.wait_for(lambda: 
      self.check_for_row_in_game_table("1: 11-3 : Andrea") )
    self.wait_for(lambda: 
      self.check_for_row_in_game_table("2: 2-11 : Diego") )


  def test_cannot_add_duplicate_games(self):
    # Ana starts a new list. 
    self.browser.get(self.live_server_url)
    self.get_game_input_box().send_keys("4-7 : Paulina")
    self.get_game_input_box().send_keys(Keys.ENTER)
    self.wait_for(lambda: 
      self.check_for_row_in_game_table("1: 4-7 : Paulina"))
    
    # She accidentally tries to enter a duplicate game. 
    self.get_game_input_box().send_keys("4-7 : Paulina")
    self.get_game_input_box().send_keys(Keys.ENTER)
    self.wait_for(lambda: self.assertEqual(
      self.browser.find_element_by_css_selector(".has-error").text,
      "You've already entered this game."))
    