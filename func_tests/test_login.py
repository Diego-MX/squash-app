from django.core import mail
from selenium.webdriver.common.keys import Keys
import re 

from .base import FunctionalTest

TEST_EMAIL = "test_anastasia@yahoo.com"
SUBJECT = "Login link for Squashitlan"


class LoginTest(FunctionalTest):
  def test_can_get_email_link_to_login(self):
    # Ana ve la funcionalidad de Login en la pagina de Squashitlan.
    # Naturalmente ingresa su correo. 
    self.browser.get(self.live_server_url)
    self.browser.find_element_by_name("email").send_keys(TEST_EMAIL)
    self.browser.find_element_by_name("email").send_keys(Keys.ENTER)

    # Aparece un mensaje de que recibió un correo. 
    self.wait_for(lambda: self.assertIn("Check your email", 
      self.browser.find_element_by_tag_name("body").text ))
    
    # Se emete a su correo y encuentra el mensaje. 
    email = mail.outbox[0]
    self.assertIn(TEST_EMAIL, email.to)
    self.assertEqual(SUBJECT, email.subject)

    # Y tiene un URL el correo. 
    self.assertIn("Use this link to log in", email.body)
    url_search = re.search(r"http://.+/.*$", email.body)

    if not url_search:
      self.fail(f"Could not find url in email bodyt:\n{ email.body }")
    url = url_search.group(0)  
    self.assertIn(self.live_server_url, url)

    # Le da click. 
    self.browser.get(url)

    # Entró a la página. 
    self.wait_for(lambda: self.browser.find_element_by_link_text("Log out"))
    navbar = self.browser.find_element_by_css_selector(".navbar")
    self.assertIn(TEST_EMAIL, navbar.text)

    
