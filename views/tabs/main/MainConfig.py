from utilities.StateInterfaces import IRestorable, ISavable
from views import Application
from views.tabs import TkViewElements
from views.tabs.main.tab_sections import IntervalConfig, OptionalConfig, ServerFunctions, ServerInfo


class MainConfig(TkViewElements.TkTab, ISavable, IRestorable):
    """
    Tab Element, has subordinate elements

    Creates and tracks the following components: Interval Configs, Optional Configs, Server Info, and Server Functions
    """

    interval_config: IntervalConfig = None
    optional_config: OptionalConfig = None
    server_info: ServerInfo = None
    server_functions: ServerFunctions = None

    def __init__(self, application: 'Application.Application', tab_name: str = "Main", index: int = 0):
        super().__init__(application.get_tab_control(), tab_name, index)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.application: Application = application
        self.create_subcomponents()

    def create_subcomponents(self):
        self.interval_config = IntervalConfig.IntervalConfig(self)
        self.optional_config = OptionalConfig.OptionalConfig(self)
        self.server_info = ServerInfo.ServerInfo(self)
        self.server_functions = ServerFunctions.ServerFunctions(self)

    def save(self) -> dict:
        return self.interval_config.save() | self.optional_config.save()

    def restore(self, restore_data: dict) -> None:
        self.interval_config.restore(restore_data)
        self.optional_config.restore(restore_data)
        self.server_info.update_server_info()
