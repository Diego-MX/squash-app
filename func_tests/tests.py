from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

import unittest
import time

MAX_WAIT = 10


# class NewVisitorTest(unittest.TestCase): 
class NewVisitorTest(LiveServerTestCase):

  def setUp(self): 
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def check_for_row_in_game_table(self, row_text):
    table = self.browser.find_element_by_id("id_game_table")
    rows  = table.find_elements_by_tag_name("tr")
    self.assertIn(row_text, [row.text for row in rows],
      f"New game does not appear in table. Contents were:\n{table.text}" )

  def wait_for_row_in_game_table(self, row_text):
    start_time = time.time()
    while True:
      try: 
        table = self.browser.find_element_by_id("id_game_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertIn(row_text, [a_row.text for a_row in rows])
        return
      except (AssertionError, WebDriverException) as err:
        if time.time() - start_time > MAX_WAIT:
          raise err
        time.sleep(0.5)

  def test_games_for_one_player(self):
    # Ana quiere entrar a la página del squash.
    # self.browser.get("http://localhost:8000")
    self.browser.get(self.live_server_url) 
    
    # Ana verifica que el título y el header digan Juegos. 
    self.assertIn("Games played", self.browser.title)
    header_text = self.browser.find_element_by_tag_name("h1").text
    self.assertIn("New player", header_text)    

    ## Recuadros para: tu nombre, el juego.  Submit. 
    # playerinput = self.browser.find_element_by_id("id_new_player")
    # self.assertEqual(playerinput.get_attribute("placeholder"), 
    #     "Your name?")

    # Hay un recuadro para ingresar juegos. 
    inputbox = self.browser.find_element_by_id("id_new_game") 
    self.assertEqual(inputbox.get_attribute("placeholder"), 
        "Enter game as: 'Score : AgainstPlayer'")

    # Ana ingresa su primer juego contra Pablo. Pierde 6-11  
    inputbox.send_keys("6-11 : Pablo")

    # Al darle enter se queda guardado el juego.
    inputbox.send_keys(Keys.ENTER)
    self.wait_for_row_in_game_table("1: 6-11 : Pablo")
    
    # Todavía hay un cuadro para ingresar más juegos. 
    # Ingresa un juego contra Paulina. Gana 11-8
    inputbox = self.browser.find_element_by_id("id_new_game")
    inputbox.send_keys("11-8 : Paulina")
    inputbox.send_keys(Keys.ENTER)
    
    # La página se actualiza. Se ven los dos juegos. 
    self.wait_for_row_in_game_table("1: 6-11 : Pablo")
    self.wait_for_row_in_game_table("2: 11-8 : Paulina")

    # Sólo faltó:  Visita el URL y sigue viendo los juegos. 

    # Satisfecha se va a dormir. 


  def test_multiple_players_different_games(self):
    # Ana makes the usual games list. 
    self.browser.get(self.live_server_url)
    inputbox = self.browser.find_element_by_id("id_new_game")
    inputbox.send_keys("6-11 : Pablo")
    inputbox.send_keys(Keys.ENTER)
    self.wait_for_row_in_game_table("1: 6-11 : Pablo")
  
    # She asks herself if the site remembers previous games. Finds the URL and goes to dinner. 
    url_juegos_ana = self.browser.current_url
    self.assertRegex(url_juegos_ana, "/players/.+")
    self.browser.quit()
    ## Quit browser to erase cookies from previoues session.

    # Bernardo gets to the site and sees no sign of Ana's games. 
    self.browser = webdriver.Firefox()
    self.browser.get(self.live_server_url)
    page_text = self.browser.find_element_by_tag_name("body").text
    self.assertNotIn("6-11 : Pablo", page_text)
    self.assertNotIn("11-8 : Paulina", page_text)

    # Bernardo enters his own games. 
    inputbox = self.browser.find_element_by_id("id_new_game")
    inputbox.send_keys("11-3 : Coach")
    inputbox.send_keys(Keys.ENTER)
    self.wait_for_row_in_game_table("1: 11-3 : Coach")

    # Bernardo tiene su propio URL diferente de Ana. 
    url_juegos_bernardo = self.browser.current_url
    self.assertRegex(url_juegos_bernardo, "/players/.+")
    self.assertNotEqual(url_juegos_bernardo, url_juegos_ana)

    # De nuevo, ningún rastro de los juegos de Ana. 
    page_text = self.browser.find_element_by_tag_name("body").text
    self.assertNotIn("6-11 : Pablo", page_text)
    self.assertIn("11-3 : Coach", page_text)

    # Satisfechos se van a dormir. 
    
  def test_layout_and_styling(self):
    # Ana visits the home page. 
    self.browser.get(self.live_server_url)
    self.browser.set_window_size(1024, 768)

    # She notices the input box is nicely centered
    inputbox = self.browser.find_element_by_id("id_new_game")
    self.assertAlmostEqual(
        inputbox.location["x"] + inputbox.size["width"]/2, 
        512, delta=10 )

    # She enters a new game and sees the input is centere there too
    inputbox.send_keys("test game")
    inputbox.send_keys(Keys.ENTER)
    self.wait_for_row_in_game_table("1: test game")
    inputbox = self.browser.find_element_by_id("id_new_game")
    self.assertAlmostEqual(
        inputbox.location["x"] + inputbox.size["width"]/2, 
        512, delta=10 )




