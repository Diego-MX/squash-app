from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest
import time

class NewVisitorTest(unittest.TestCase): 

  def setUp(self): 
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()


  def test_starts_game_and_retrieves_later(self):
    # Ana quiere entrar a la página del squash. 
    self.browser.get("http://localhost:8000")

    # Ana verifica que el título y el header digan Juegos. 
    self.assertIn("Games played", self.browser.title)
    header_text = self.browser.find_element_by_tag_name("h1").text
    self.assertIn("Games played", header_text)    

    # Hay un recuadro para ingresar juegos. 
    inputbox = self.browser.find_element_by_id("id_new_item") 
    self.assertEqual(inputbox.get_attribute("placeholder"), 
        "Enter a game as:  'Score; AgainstPlayer'")

    # Ana ingresa su primer juego contra Pablo. Pierde 6-11  
    inputbox.send_keys("6-11; Pablo")

    # Al darle enter se queda guardado el juego.
    inputbox.send_keys(Keys.ENTER)
    time.sleep(1)

    table = self.browser.find_element_by_id("id_list_table")
    rows = table.find_elements_by_tag_name("tr")
    self.assertTrue(
      any(row.text == "1: 6-11; Pablo" for row in rows) )

    # Todavía hay un cuadro para ingresar más juegos. 

    self.fail("Finish the test!")
  
  # Ingresa un juego contra Paulina. Gana 11-8

  # La página se actualiza. Se ven los dos juegos. 

  # Se pregunta si el sitio recuerda los juegos.  Encuentra el URL. 

  # Visita el URL y sigue viendo los juegos. 


if __name__ == "__main__":
  unittest.main(warnings="ignore")


