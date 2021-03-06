from django.test import TestCase
from unittest.mock import patch, call
from accounts.models import Token
import accounts.views


class SendLoginEmailViewTest(TestCase):
  def test_redirects_to_homepage(self):
    a_response = self.client.post("/accounts/send_login_email", 
        data = {"email": "test_user@example.com"} )
    self.assertRedirects(a_response, "/")


  @patch("accounts.views.send_mail")
  def test_emails_address_from_post(self, mock_send_mail):
    self.client.post("/accounts/send_login_email", 
        data = {"email": "test_user@example.com"} )
    
    self.assertTrue(mock_send_mail.called) 
    (m_subject, m_body, m_from, m_to), _kwargs = mock_send_mail.call_args
    self.assertEqual(m_subject, "Login link for Squashitlan")
    self.assertEqual(m_from, "diego.villamil@squashitlan.com")
    self.assertEqual(m_to,  ["test_user@example.com"])


  @patch('accounts.views.messages')
  def test_adds_success_message_with_mocks(self, mock_messages):
    response = self.client.post('/accounts/send_login_email', 
        data = {'email': 'test_user@example.com'} )
    expected = "Check your email, we've sent you a link to log in."
    self.assertEqual( mock_messages.success.call_args,
        call(response.wsgi_request, expected), )


  def test_creates_token_associated_with_email(self):
    self.client.post('/accounts/send_login_email', 
        data={'email': 'test_user@example.com'})
    token = Token.objects.first()
    self.assertEqual(token.email, 'test_user@example.com')


  @patch('accounts.views.send_mail')
  def test_sends_link_to_login_using_token_uid(self, mock_send_mail):
    self.client.post('/accounts/send_login_email', 
        data={'email': 'test_user@example.com'} )
    token = Token.objects.first()
    expected_url = f'http://testserver/accounts/login?token={token.uid}'
    (subject, body, from_email, to_list), _kwargs = mock_send_mail.call_args
    self.assertIn(expected_url, body)


@patch('accounts.views.auth')
class LoginViewTest(TestCase):

  def test_redirects_to_home_page(self, mock_auth):
    response = self.client.get('/accounts/login?token=abcd123')
    self.assertRedirects(response, '/')
  
  def test_calls_authenticate_with_uid_from_get_request(self, mock_auth):
    self.client.get('/accounts/login?token=abcd123')
    self.assertEqual(mock_auth.authenticate.call_args, call(uid='abcd123'))

  def test_call_returns_user_with_email(self, mock_auth):
    response = self.client.get("/accounts/login?token=abcd123")
    self.assertEqual(mock_auth.login.call_args, 
        call(response.wsgi_request, mock_auth.authenticate.return_value ))

  def test_does_not_login_if_user_is_not_authenticated(self, mock_auth):
    mock_auth.authenticate.return_value = None  
    self.client.get('/accounts/login?token=abcd123')
    self.assertFalse(mock_auth.login.called)  






