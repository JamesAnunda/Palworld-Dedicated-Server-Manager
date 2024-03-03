from controllers.tabs.main import MainController
from utilities.StateInterfaces import IRestorable, ISavable


class MainModel(ISavable, IRestorable):
    def __init__(self, controller: 'MainController.MainController'):
        self.controller: MainController = controller

    def save(self) -> dict:
        return {}

    def restore(self, restore_data: dict) -> None:
        pass
