from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase): 

  def setUp(self): 
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_starts_game_and_retrieves_later(self):
    # Ana quiere entrar a la página del squash. 
    self.browser.get("http://localhost:8000")

    # Ana verifica que el título diga juegos. 
    self.assertIn("Games", self.browser.title)
    self.fail("Finish the test!")

  # Ana ingresa su primer juego contra Pablo. Pierde 6-11

  # Al darle enter se queda guardado el juego. 

  # Todavía hay un cuadro para ingresar más juegos. 

  # Ingresa un juego contra Paulina. Gana 11-8

  # La página se actualiza. Se ven los dos juegos. 

  # Se pregunta si el sitio recuerda los juegos.  Encuentra el URL. 

  # Visita el URL y sigue viendo los juegos. 


if __name__ == "__main__":
  unittest.main(warnings="ignore")


