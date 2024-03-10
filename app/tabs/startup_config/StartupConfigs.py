from app import Application
from app.tabs.startup_config.sections import PalWorldSettings, ServerConfigs
from app.utilities import TkViewElements
from app.utilities.StateInterfaces import IRestorable, ISavable


class StartupConfigs(TkViewElements.TkTab, ISavable, IRestorable):
    """
    Tab Element, has subordinate elements

    Creates and tracks the following components: Interval Configs, Optional Configs, Server Info, and Server Functions
    """
    world_settings: PalWorldSettings = None
    server_configs: ServerConfigs = None

    def __init__(self, application: 'Application.Application', tab_name: str = "Startup Configs"):
        super().__init__(application.get_tab_control(), tab_name)
        self.application: Application = application
        self.columnconfigure(0, weight=1)
        self.create_subcomponents()

    def create_subcomponents(self) -> None:
        self.world_settings = PalWorldSettings.PalWorldSettings(self, self.application.settings_handler)
        self.server_configs = ServerConfigs.ServerConfigs(self, self.application.settings_handler)

    def save(self) -> None:
        self.server_configs.save()
        self.world_settings.save()

    def restore(self) -> None:
        self.world_settings.restore()
        self.server_configs.restore()

    def append_output(self, message) -> None:
        self.application.append_output(message)
