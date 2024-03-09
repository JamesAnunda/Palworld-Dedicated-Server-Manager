from app import Application
from app.tabs.main.sections import IntervalConfig, OptionalConfig, SaveConfigs, ServerFunctions, ServerInfo
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
    save_configs: SaveConfigs = None

    def __init__(self, application: 'Application.Application', tab_name: str = "Main"):
        super().__init__(application.get_tab_control(), tab_name, index=[0, 1])
        self.application: Application = application
        self.create_subcomponents()

    def create_subcomponents(self) -> None:
        self.interval_config: IntervalConfig = IntervalConfig.IntervalConfig(self, self.application.settings_handler)
        self.optional_config: OptionalConfig = OptionalConfig.OptionalConfig(self, self.application.settings_handler)
        self.server_info: ServerInfo = ServerInfo.ServerInfo(self, self.application.settings_handler)
        self.server_functions: ServerFunctions = ServerFunctions.ServerFunctions(self)
        self.save_configs: SaveConfigs = SaveConfigs.SaveConfigs(self, self.application.settings_handler)

    def save(self) -> None:
        self.interval_config.save()
        self.optional_config.save()
        self.server_info.save()
        self.save_configs.save()

    def restore(self) -> None:
        self.save_configs.restore()
        self.interval_config.restore()
        self.optional_config.restore()
        self.server_info.restore()
        self.server_info.update_server_info()

    def append_output(self, message) -> None:
        self.application.append_output(message)

    def interval_restart_enabled(self):
        return self.interval_config.interval_restart_enabled()

    def daily_restart_enabled(self):
        return self.interval_config.daily_restart_enabled()

    def monitor_interval_enabled(self):
        return self.interval_config.monitor_interval_enabled()

    def backup_interval_enabled(self):
        return self.interval_config.backup_interval_enabled()

    def email_notification_enabled(self):
        return self.optional_config.email_notification_enabled()

    def discord_notification_enabled(self):
        return self.optional_config.discord_notification_enabled()

    def startup_update_check_enabled(self):
        return self.optional_config.startup_update_check_enabled()

    def backup_during_restart_enabled(self):
        return self.optional_config.backup_during_restart_enabled()

    def delete_old_backups_enabled(self):
        return self.optional_config.delete_old_backups_enabled()
