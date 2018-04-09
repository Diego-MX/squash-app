from .base import FunctionalTest

from selenium.webdriver.common.keys import Keys


class LayoutAndStylingTest(FunctionalTest):
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

