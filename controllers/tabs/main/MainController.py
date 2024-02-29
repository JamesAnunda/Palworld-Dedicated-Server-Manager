from tkinter import ttk

from controllers.ApplicationController import ApplicationController
from models.tabs.main.MainModel import MainModel
from views.tabs.main.MainView import MainView


class MainController:
    def __init__(self, parent_controller: ApplicationController, tab_control: ttk.Notebook):
        self.parent_controller: ApplicationController = parent_controller
        self.model: MainModel = MainModel(self)
        self.view: MainView = MainView(self, tab_control)
        pass

    def get_model(self) -> MainModel:
        return self.model

    def get_view(self) -> MainView:
        return self.view
