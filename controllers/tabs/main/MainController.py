from tkinter import ttk

from controllers.ApplicationController import ApplicationController
from models.tabs.main.MainModel import MainModel
from views.tabs.main.MainView import MainView


class MainController:
    def __init__(self, parent_controller: ApplicationController):
        self.parent_controller: ApplicationController = parent_controller
        self.model: MainModel = MainModel(self)
        self.view: MainView = MainView(self)

    def get_model(self) -> MainModel:
        return self.model

    def get_view(self) -> MainView:
        return self.view

    def get_tab_control(self) -> ttk.Notebook:
        return self.parent_controller.get_tab_control()
