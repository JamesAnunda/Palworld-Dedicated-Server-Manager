import json
from typing import TextIO


class SettingsItem:
    def __init__(self, current_value, default_value):
        self.__current_value = current_value
        self.__default_value = default_value if default_value is not None else ""

    def get(self) -> str:
        """
        Return the current value, or the default value if current value is None. Default value will always have a value or be '' (empty string)
        """
        return self.__current_value if (self.__current_value is not None and self.__current_value != "") else self.__default_value

    def set(self, new_value) -> None:
        self.__current_value = new_value if new_value is not None else self.__default_value

    def get_default(self) -> str:
        return self.__default_value

class SettingsHandler(dict):
    def __init__(self):
        super().__init__()
        self.interval_restart_hours = SettingsItem("", "")
        self.daily_restart_time = SettingsItem("", "12:00 AM")
        self.monitor_interval_minutes = SettingsItem("", "")
        self.backup_interval_hours = SettingsItem("", "")
        self.delete_old_backups_days = SettingsItem("", "")
        self.external_ip = SettingsItem("", "127.0.0.1")

        self.arrcon_directory = SettingsItem("", "No Directory Selected")
        self.backup_directory = SettingsItem("", "No Directory Selected")
        self.palworld_directory = SettingsItem("", "No Directory Selected")
        self.steamcmd_directory = SettingsItem("", "No Directory Selected")
        self.server_start_args = SettingsItem("", "-useperfthreads -NoAsyncLoadingThread -UseMultithreadForDS -EpicApp=PalServer")

        self.email_address = SettingsItem("", "")
        self.smtp_server = SettingsItem("", "smtp.gmail.com")
        self.smtp_port = SettingsItem("", "587")
        self.discord_webhook = SettingsItem("", "")

    def __getattr__(self, attr):
        if attr in self:
            return self[attr]
        else:
            raise AttributeError(attr)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self) -> dict[str, str]:
        return dict((setting, self[setting].get()) for setting in self.keys())

    def restore(self, file: TextIO):
        settings = json.load(file)
        for setting in self.keys():
            self[setting].set(settings.get(setting))
