from utilities import TkViewElements
from utilities.StateInterfaces import IRestorable, ISavable
from views import Application
from views.tabs.server_config.tab_sections import PalWorldSettings, ServerConfigs


class StartupConfigs(TkViewElements.TkTab, ISavable, IRestorable):
    """
    Tab Element, has subordinate elements

    Creates and tracks the following components: Interval Configs, Optional Configs, Server Info, and Server Functions
    """

    world_settings: PalWorldSettings = None
    server_configs: ServerConfigs = None

    def __init__(self, application: 'Application.Application', tab_name: str = "Startup Configs", index: int = 1):
        super().__init__(application.get_tab_control(), tab_name, index)
        self.application: Application = application
        self.columnconfigure(0, weight=1)
        self.create_subcomponents()

    def create_subcomponents(self):
        self.world_settings = PalWorldSettings.PalWorldSettings(self)
        self.server_configs = ServerConfigs.ServerConfigs(self)

    def save(self) -> dict:
        return self.server_configs.save()

    def restore(self, restore_data: dict) -> None:
        self.world_settings.restore(restore_data)
        self.server_configs.restore(restore_data)
