#from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

from unittest import skip

import os
import unittest
import time

MAX_WAIT = 10


class FunctionalTest(StaticLiveServerTestCase):
  def setUp(self): 
    self.browser   = webdriver.Firefox()
    staging_server = os.environ.get("STAGING_SERVER")
    if staging_server: 
      # LIVE_SERVER_URL ya existe, pero se modifica. 
      self.live_server_url = "http://" + staging_server


  def tearDown(self):
    self.browser.quit()


  def wait_for(self, a_function):
    start_time = time.time()
    while True:
      try: 
        return a_function()
      except (AssertionError, WebDriverException) as an_error:
        if time.time() - start_time > MAX_WAIT:
          raise an_error
        time.sleep(0.5)


  def check_for_row_in_game_table(self, row_text):
    table = self.browser.find_element_by_id("id_game_table")
    rows = table.find_elements_by_tag_name("tr")
    self.assertIn(row_text, [a_row.text for a_row in rows])


  def wait_for_row_in_game_table(self, row_text):
    start_time = time.time()
    while True:
      try: 
        table = self.browser.find_element_by_id("id_game_table")
        rows = table.find_elements_by_tag_name("tr")
        self.assertIn(row_text, [a_row.text for a_row in rows])
        return
      except (AssertionError, WebDriverException) as err:
        if time.time() - start_time > MAX_WAIT:
          raise err
        time.sleep(0.5)


  def get_game_input_box(self):
    return self.browser.find_element_by_id('id_text')


