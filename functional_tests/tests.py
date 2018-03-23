from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest
import time

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


  def test_starts_game_and_retrieves_later(self):
    # Ana quiere entrar a la página del squash.
    # self.browser.get("http://localhost:8000")
    self.browser.get(self.live_server_url) 
    

    # Ana verifica que el título y el header digan Juegos. 
    self.assertIn("Games played", self.browser.title)
    header_text = self.browser.find_element_by_tag_name("h1").text
    self.assertIn("Games played", header_text)    

    # Hay un recuadro para ingresar juegos. 
    inputbox = self.browser.find_element_by_id("id_new_game") 
    self.assertEqual(inputbox.get_attribute("placeholder"), 
        "Enter a game as:  'Score : AgainstPlayer'")

    # Ana ingresa su primer juego contra Pablo. Pierde 6-11  
    inputbox.send_keys("6-11 : Pablo")

    # Al darle enter se queda guardado el juego.
    inputbox.send_keys(Keys.ENTER)
    time.sleep(1)
    self.check_for_row_in_game_table("1: 6-11 : Pablo")
    
    # Todavía hay un cuadro para ingresar más juegos. 
    # Ingresa un juego contra Paulina. Gana 11-8
    inputbox = self.browser.find_element_by_id("id_new_game")
    inputbox.send_keys("11-8 : Paulina")
    inputbox.send_keys(Keys.ENTER)
    time.sleep(1)

    # La página se actualiza. Se ven los dos juegos. 
    self.check_for_row_in_game_table("1: 6-11 : Pablo")
    self.check_for_row_in_game_table("2: 11-8 : Paulina")

    # Se pregunta si el sitio recuerda los juegos.  Encuentra el URL. 

    # Visita el URL y sigue viendo los juegos. 

    self.fail("Finish the test!")

  

if __name__ == "__main__":
  unittest.main(warnings="ignore")


