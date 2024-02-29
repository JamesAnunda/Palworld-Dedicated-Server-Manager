from controllers.tabs.about import AboutController
from controllers.tabs.alerts_config import AlertsConfigController
from controllers.tabs.main.MainController import MainController
from controllers.tabs.server_config import ServerConfigController
from models.ApplicationModel import ApplicationModel
from views.ApplicationView import ApplicationView


class ApplicationController:
    def __init__(self):
        self.model: ApplicationModel = ApplicationModel(self)
        self.view: ApplicationView = ApplicationView(self)
        # sub-controllers, each handles their own view & model; only controllers communicate directly through layer
        self.main_controller: MainController = MainController(self, self.view.tab_control)
        self.server_config_controller = None
        self.alerts_config_controller = None
        self.about_controller = None

    def get_model(self) -> ApplicationModel:
        return self.model

    def get_view(self) -> ApplicationView:
        return self.view

    def get_main_controller(self) -> MainController:
        return self.main_controller

    def get_server_config_controller(self) -> ServerConfigController:
        return self.server_config_controller

    def get_alerts_config_controller(self) -> AlertsConfigController:
        return self.alerts_config_controller

    def get_about_controller(self) -> AboutController:
        return self.about_controller
