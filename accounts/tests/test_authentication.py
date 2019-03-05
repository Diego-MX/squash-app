from django.test import TestCase 
from django.contrib.auth import get_user_model
from accounts.authentication import PasswordlessAuthenticationBackend as pwdlessBackend
from accounts.models import Token

User = get_user_model()



class AuthenticateTest(TestCase):
  def test_returns_None_if_no_token(self):
    the_user = pwdlessBackend().authenticate("no-such-token")
    self.assertIsNone(the_user)
  
  def test_returns_new_user_from_email_if_token(self):
    an_email = "test_user@example.com"
    token = Token.objects.create(email=an_email)
    new_user = pwdlessBackend().authenticate(token.uid)
    the_user = User.objects.get(email=an_email)
    self.assertEqual(the_user, new_user)

  def test_returns_existing_user_from_email_if_token(self):
    an_email = "test_user@example.com"
    existing_user = User.objects.create(email=an_email)
    token = Token.objects.create(email=an_email)
    the_user = pwdlessBackend().authenticate(token.uid)
    self.assertEqual(the_user, existing_user)


class GetUserTest(TestCase):
  def test_get_user_by_email(self):
    User.objects.create(email="second_test@example.com")
    existing_user = User.objects.create(email="test_user@example.com")
    the_user = pwdlessBackend().get_user(email="test_user@example.com")
    self.assertEqual(the_user, existing_user)

  def test_returns_None_if_no_user_email(self):
    the_user = pwdlessBackend().get_user(email="test_user@example.com")
    self.assertIsNone(the_user)







