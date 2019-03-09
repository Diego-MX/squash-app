from django.core import mail
from selenium.webdriver.common.keys import Keys
import os, poplib, re, time


from .base import FunctionalTest

# TEST_EMAIL = 'test_anastasia@yahoo.com'
SUBJECT = 'Login link for Squashitlan'


class LoginTest(FunctionalTest):

  def wait_for_email(self, test_email, subject): 
    if not self.staging_server:
      email = mail.outbox[0]
      self.assertIn(test_email, email.to)
      self.assertEqual(email.subject, subject)
      the_body = email.body
    else:
      time.sleep(10)
      email_id = None 
      inbox = poplib.POP3_SSL('pop.mail.yahoo.com')
      try:
        inbox.user(test_email)
        inbox.pass_(os.environ['TEST_USER_PASSWORD'])
        m_count, _ = inbox.stat() 
        for i_msg in range(m_count, max(m_count-5, 0),-1):
          _, m_lines, __ = inbox.retr(i_msg)
          m_lines = [each.decode('utf8') for each in m_lines]
          if f'Subject: {subject}' in m_lines:
            email_id = i_msg
            the_body = '\n'.join(m_lines)
      except: 
        the_body = None
      finally:
        if email_id:
          inbox.dele(email_id)
        inbox.quit()
    return the_body


  def test_can_get_email_link_to_login(self):
    # Ana ve la funcionalidad de Login en la pagina de Squashitlan.
    # Naturalmente ingresa su correo. 
    if self.staging_server:
      test_email = 'test_anastasia@yahoo.com'
    else:
      test_email = 'anastasia@example.com'
    
    self.browser.get(self.live_server_url)
    self.browser.find_element_by_name('email').send_keys(test_email)
    self.browser.find_element_by_name('email').send_keys(Keys.ENTER)

    # Aparece un mensaje de que recibió un correo. 
    self.wait_for(lambda: self.assertIn('Check your email', 
      self.browser.find_element_by_tag_name('body').text ))
    
    # Se mete a su correo y encuentra el mensaje. 
    body = self.wait_for_email(test_email, SUBJECT)

    # Y tiene un URL el correo. 
    self.assertIn('Use this link to log in', body)
    url_search = re.search(r'http://.+/.*$', body)

    if not url_search:
      self.fail(f'Could not find url in email bodyt:\n{body}')
    url = url_search.group(0)  
    self.assertIn(self.live_server_url, url)

    # Le da click. 
    self.browser.get(url)

    # Entró a la página. 
    self.wait_for_being_logged_in(email=test_email)
    
    # She logs out. 
    self.browser.find_element_by_link_text('Log out').click()

    # She is logged out
    self.wait_for_being_logged_out(email=test_email)
    

  
  
    

    
