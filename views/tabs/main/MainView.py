from tkinter import ttk

from controllers.tabs.main.MainController import MainController
from views.tabs import TkViewElements


class MainView(TkViewElements.TkTab):
    def __init__(self, controller: MainController, tab_control: ttk.Notebook, tab_name: str = "Main", index: int = 0):
        super().__init__(tab_control, tab_name, index)
        self.controller: MainController = controller
