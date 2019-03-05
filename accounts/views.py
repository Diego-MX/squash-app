from django.contrib import auth, messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse 
from django.shortcuts import redirect, render
from accounts.models import Token


def send_login_email(request):
  an_email = request.POST["email"]
  token = Token.objects.create(email=an_email)
  url = request.build_absolute_uri("{}?token={}".\
      format(reverse("login"), str(token.uid)))
  message_body = f"Use this link to log in:\n\n{ url }"
  send_mail(
      "Login link for Squashitlan", 
      message_body, 
      "diego.villamil@squashitlan.com", 
      [an_email])
  messages.success(request, 
      "Check your email, we've sent you a link to log in.")
  response = redirect("/")
  return response

def login(request):
  token_id = request.GET.get("token")
  user = auth.authenticate(uid=token_id)
  if user is not None:
    auth.login(request, user)
  response = redirect("/")
  return response

  



