
from .base import FunctionalTest

from selenium.webdriver.common.keys import Keys
from unittest import skip
import time

class GameValidationTest(FunctionalTest):
  
  def get_error_element(self):
    the_error = self.browser.find_element_by_css_selector(".has-error")
    return the_error


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
    # Ana logs in. 
    self.browser.get(self.live_server_url)
    self.get_game_input_box().send_keys("11-3 : Pablo")
    self.get_game_input_box().send_keys(Keys.ENTER)
    self.wait_for(lambda:
      self.check_for_row_in_game_table("1: 11-3 : Pablo"))
    
    # She wants to duplicate item. 
    self.get_game_input_box().send_keys("11-3 : Pablo")
    self.get_game_input_box().send_keys(Keys.ENTER)
    
    # She sees a helpful message
    self.wait_for(lambda: self.assertEqual(
      self.get_error_element().text,
      "You've saved this game already." ))


  def test_error_messages_cleared_on_input(self):
    # Ana  guarda sus juegos y causa un error. 
    self.browser.get(self.live_server_url)
    self.get_game_input_box().send_keys("4-11 : Rodrigo")
    self.get_game_input_box().send_keys(Keys.ENTER)
    self.wait_for(lambda: 
      self.check_for_row_in_game_table("1: 4-11 : Rodrigo") )
    self.get_game_input_box().send_keys("4-11 : Rodrigo")
    self.get_game_input_box().send_keys(Keys.ENTER)
    
    self.wait_for(lambda: self.assertTrue(
      self.get_error_element().is_displayed() ))

    # Empieza a escribir y se borra el error. 
    self.get_game_input_box().send_keys("8")
    
    # Está contenta de que el error desaparezca. 
    self.wait_for(lambda: self.assertFalse(
      self.get_error_element().is_displayed() ))


