import json
import os
from typing import TextIO


class SettingsItem:
    def __init__(self, current_value, default_value):
        self.__current_value = current_value
        self.__default_value = default_value if default_value is not None else ""

    def get(self) -> str:
        """
        Return the current value, or the default value if current value is None. Default value will always have a value or be '' (empty string)
        """
        return self.__current_value if self.__current_value is not None and self.__current_value != "" else self.__default_value

    def set(self, new_value) -> None:
        self.__current_value = new_value if new_value is not None else self.__default_value

    def get_default(self) -> str:
        return self.__default_value

    def is_default(self) -> bool:
        return self.get() == self.__default_value


class SettingsHandler(dict):
    def __init__(self):
        super().__init__()
        self.interval_restart_hours = SettingsItem("", "")
        self.interval_restart_enabled = SettingsItem(False, False)
        self.daily_restart_time = SettingsItem("", "12:00 AM")
        self.daily_restart_enabled = SettingsItem(False, False)
        self.monitor_interval_minutes = SettingsItem("", "")
        self.monitor_interval_enabled = SettingsItem(False, False)
        self.backup_interval_hours = SettingsItem("", "")
        self.backup_interval_enabled = SettingsItem(False, False)

        self.send_email_on_crash_enabled = SettingsItem(False, False)
        self.send_discord_on_crash_enabled = SettingsItem(False, False)
        self.check_update_on_start_enabled = SettingsItem(False, False)
        self.backup_on_restart_enabled = SettingsItem(False, False)
        self.delete_old_backups_days = SettingsItem("", "")
        self.delete_old_backups_enabled = SettingsItem(False, False)

        self.external_ip = SettingsItem("", "127.0.0.1")

        self.arrcon_location = SettingsItem("", "No Directory Selected")
        self.backup_location = SettingsItem("", "No Directory Selected")
        self.palworld_location = SettingsItem("", "No Directory Selected")
        self.steamcmd_location = SettingsItem("", "No Directory Selected")
        self.server_start_args = SettingsItem("", "-useperfthreads -NoAsyncLoadingThread -UseMultithreadForDS -EpicApp=PalServer")

        self.rcon_port = SettingsItem("", "")
        self.rcon_pass = SettingsItem("", "")

        self.settings_location = SettingsItem("", os.path.join(os.path.expanduser("~"), "Documents\\Palworld Server Manager", "settings.json"))
        self.email_address = SettingsItem("", "")
        self.email_password = SettingsItem("", "")
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

    def save(self) -> None:
        os.makedirs(os.path.split(self.settings_location.get())[0], exist_ok=True)
        settings = dict((setting, self[setting].get()) for setting in self.keys() if self[setting] != self.email_password)
        with open(self.settings_location.get(), "w") as file:
            json.dump(settings, file, indent=4, sort_keys=True)

    def restore(self, file: TextIO):
        settings = json.load(file)
        for setting in self.keys():
            self[setting].set(settings.get(setting))
