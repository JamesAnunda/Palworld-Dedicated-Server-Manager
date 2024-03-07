from app import Application
from app.tabs.main.sections import IntervalConfig, OptionalConfig, ServerFunctions, ServerInfo
from app.utilities import TkViewElements
from app.utilities.StateInterfaces import IRestorable, ISavable


class MainConfig(TkViewElements.TkTab, ISavable, IRestorable):
    """
    Tab Element, has subordinate elements

    Creates and tracks the following components: Interval Configs, Optional Configs, Server Info, and Server Functions
    """

    interval_config: IntervalConfig = None
    optional_config: OptionalConfig = None
    server_info: ServerInfo = None
    server_functions: ServerFunctions = None

    def __init__(self, application: 'Application.Application', tab_name: str = "Main"):
        super().__init__(application.get_tab_control(), tab_name, index=[0, 1])
        self.application: Application = application
        self.create_subcomponents()

    def create_subcomponents(self) -> None:
        self.interval_config: IntervalConfig = IntervalConfig.IntervalConfig(self, self.application.settings_handler)
        self.optional_config: OptionalConfig = OptionalConfig.OptionalConfig(self, self.application.settings_handler)
        self.server_info: ServerInfo = ServerInfo.ServerInfo(self, self.application.settings_handler)
        self.server_functions: ServerFunctions = ServerFunctions.ServerFunctions(self)

    def save(self) -> None:
        self.interval_config.save()
        self.optional_config.save()
        self.server_info.save()

    def restore(self) -> None:
        self.interval_config.restore()
        self.optional_config.restore()
        self.server_info.restore()
        self.server_info.update_server_info()

    def append_output(self, message) -> None:
        self.application.append_output(message)
