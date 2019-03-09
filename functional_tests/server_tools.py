from fabric.api import run
from fabric.context_managers import settings, shell_env 

def _get_manage_python(host):
  command_str = f'~/sites/{host}/virtualenv/bin/python ~/sites/{host}/manage.py '

def reset_database(host): 
  manage_python = _get_manage_python(host)
  with settings(host_string=f'diego@{host}'):
    run(manage_python + 'flush --noinput')

def _get_server_env(host):
  env_lines = run(f'cat ~/sites/{host}/.env').splitlines()
  env_dict = dict(each.split('=') for each in env_lines if each)
  return env_dict 

def create_session_on_server(host, email):
  manage_python = _get_manage_python(host)
  with settings(host_string=f'diego@{host}'):
    env_vars = _get_server_env(host)
    with shell_env(**env_vars):
      session_key = run(manage_python + f'create_session {email}').strip()
  return session_key    
  