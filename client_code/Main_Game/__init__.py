from ._anvil_designer import Main_GameTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import time


class Main_Game(Main_GameTemplate):
  clock = time.time()
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.

  def submit_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.timer_1.interval = 0
    print(self.timer_1)
    self.clock = time.time() - self.clock
    #words = "towing towel wing goat twong toe nile"
    words = "towing towel wing tong legion tingle nile"
    fail_conditions = anvil.server.call('submit_answers', words, "toweling")
    if any(len(criteria) != 0 for criteria in fail_conditions.values()):
      open_form('Fail_Page', fail_conditions)
    else:
      print ("you did it!")
    print(round(self.clock, 3))
    pass

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    
    self.clock += 0.001
    pass




