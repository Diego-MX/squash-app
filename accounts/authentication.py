from accounts.models import User, Token 



class PasswordlessAuthenticationBackend(object):
  def authenticate(self, uid):
    try: 
      token = Token.objects.get(uid=uid)
      user = User.objects.get(email=token.email)
    except User.DoesNotExist:
      user = User.objects.create(email=token.email)
    except Token.DoesNotExist: 
      user = None
    return user 

  def get_user(self, email): 
    try: 
      user = User.objects.get(email = email)
    except User.DoesNotExist:
      user = None
    return user


