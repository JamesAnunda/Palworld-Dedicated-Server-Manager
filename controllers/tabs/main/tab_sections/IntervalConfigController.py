from controllers.tabs.main import MainController
from models.tabs.main.tab_sections.IntervalConfigModel import IntervalConfigModel
from utilities.StateInterfaces import IRestorable, ISavable
from views.tabs.main.tab_sections.IntervalConfig import IntervalConfig


class IntervalConfigController(ISavable, IRestorable):
    def __init__(self, parent_controller: 'MainController.MainController'):
        self.parent_controller = parent_controller
        self.model = IntervalConfigModel()
        self.view = IntervalConfig(self, self.parent_controller.get_view())

    def get_model(self) -> IntervalConfigModel:
        return self.model

    def get_view(self) -> IntervalConfigView:
        return self.view

    def get_parent_controller(self) -> MainController:
        return self.parent_controller

    def save(self) -> dict:
        print(self.get_model().save())
        return self.get_model().save()

    def restore(self, restore_data: dict):
        self.model.restore(restore_data)
