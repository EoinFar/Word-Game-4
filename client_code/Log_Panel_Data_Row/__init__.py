"""
  Title:      Log_Panel_Data_Row
  Author:     Eoin Farrell
  Student No: C00164354
  Purpose:    The data row for each item displayed in Log_Panel.
              The relevant data bindings are set in Log_Panel
"""


from ._anvil_designer import Log_Panel_Data_RowTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Log_Panel_Data_Row(Log_Panel_Data_RowTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
