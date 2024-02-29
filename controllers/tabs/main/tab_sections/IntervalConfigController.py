from controllers.tabs.main.MainController import MainController
from models.tabs.main.tab_sections.IntervalConfigModel import IntervalConfigModel
from views.tabs.main.tab_sections.IntervalConfigView import IntervalConfigView


class IntervalConfigController:
    def __init__(self, parent_controller: MainController):
        self.parent_controller = parent_controller
        self.model = IntervalConfigModel()
        self.view = IntervalConfigView(self.parent_controller.get_view())

    def get_model(self) -> IntervalConfigModel:
        return self.model

    def get_view(self) -> IntervalConfigView:
        return self.view
