from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

# from django.template.loader import render_to_string

from games.views import home_page


class HomePageTest(TestCase):

  def test_root_url_resolve_to_home_page_view(self):
    found = resolve("/")
    self.assertEqual(found.func, home_page)


  def test_uses_home_template(self):
    response = self.client.get("/")
    self.assertTemplateUsed(response, "home.html")
    
    ### request  = HttpRequest()
    # response = home_page(request)
    # html = response.content.decode("utf8")
    ### self.assertTrue(html.startswith("<html>"))
    # self.assertIn("<title>Games played</title>", html)  # Viene del Test funcional. 
    # self.assertTrue(html.strip().endswith("</html>"))
    ### expected_html = render_to_string("home.html")
    # self.assertEqual(html, expected_html) 

  def test_can_save_POST_request(self):
    response = self.client.post("/", 
        data={"game_text": "A new game" } )
    self.assertIn("A new game", response.content.decode())
    self.assertTemplateUsed(response, "home.html")


