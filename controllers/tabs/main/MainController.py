from tkinter import ttk

from controllers import ApplicationController
from controllers.tabs.main.tab_sections import IntervalConfigController
from models.tabs.main import MainModel
from utilities.StateInterfaces import IRestorable, ISavable


class MainController(ISavable, IRestorable):
    def __init__(self, parent_controller: 'ApplicationController.ApplicationController'):
        self.parent_controller: ApplicationController = parent_controller
        self.model: MainModel = MainModel.MainModel(self)
        self.interval_controller: IntervalConfigController = IntervalConfigController.IntervalConfigController(self)

    def get_model(self) -> MainModel:
        return self.model

    def get_parent_controller(self) -> ApplicationController:
        return self.parent_controller

    def get_tab_control(self) -> ttk.Notebook:
        return self.parent_controller.get_tab_control()

    def save(self) -> dict:
        return self.model.save() | self.interval_controller.save()

    def restore(self, restore_data: dict) -> None:
        self.model.restore(restore_data)
        self.interval_controller.restore(restore_data)
