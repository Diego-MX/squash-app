from .base import FunctionalTest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):

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
    inputbox = self.get_game_input_box() 
    self.assertEqual(inputbox.get_attribute("placeholder"), 
        "Enter game <SCORE : PLAYER_AGAINST>")

    # Ana ingresa su primer juego contra Pablo. Pierde 6-11  
    inputbox.send_keys("6-11 : Pablo")

    # Al darle enter se queda guardado el juego.
    inputbox.send_keys(Keys.ENTER)
    self.wait_for(lambda: self.check_for_row_in_game_table("1: 6-11 : Pablo"))
    
    # Todavía hay un cuadro para ingresar más juegos. 
    # Ingresa un juego contra Paulina. Gana 11-8
    inputbox = self.get_game_input_box()
    inputbox.send_keys("11-8 : Paulina")
    inputbox.send_keys(Keys.ENTER)
    
    # La página se actualiza. Se ven los dos juegos. 
    self.wait_for(lambda: self.check_for_row_in_game_table("1: 6-11 : Pablo"))
    self.wait_for(lambda: self.check_for_row_in_game_table("2: 11-8 : Paulina"))

    # Sólo faltó:  Visita el URL y sigue viendo los juegos. 

    # Satisfecha se va a dormir. 


  def test_multiple_players_different_games(self):
    # Ana makes the usual games list. 
    self.browser.get(self.live_server_url)
    inputbox = self.get_game_input_box()
    inputbox.send_keys("6-11 : Pablo")
    inputbox.send_keys(Keys.ENTER)
    self.wait_for(lambda: self.check_for_row_in_game_table("1: 6-11 : Pablo"))
  
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
    inputbox = self.get_game_input_box()
    inputbox.send_keys("11-3 : Coach")
    inputbox.send_keys(Keys.ENTER)
    self.wait_for(lambda: self.check_for_row_in_game_table("1: 11-3 : Coach"))

    # Bernardo tiene su propio URL diferente de Ana. 
    url_juegos_bernardo = self.browser.current_url
    self.assertRegex(url_juegos_bernardo, "/players/.+")
    self.assertNotEqual(url_juegos_bernardo, url_juegos_ana)

    # De nuevo, ningún rastro de los juegos de Ana. 
    page_text = self.browser.find_element_by_tag_name("body").text
    self.assertNotIn("6-11 : Pablo", page_text)
    self.assertIn("11-3 : Coach", page_text)

    # Satisfechos se van a dormir. 

