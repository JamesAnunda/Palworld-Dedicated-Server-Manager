import os
import tkinter as tk
from tkinter import ttk

from app import OutputConsole
from app.handlers.SettingsHandler import SettingsHandler
from app.tabs.about import About
from app.tabs.alerts_config import AlertsConfig
from app.tabs.main import MainConfig
from app.tabs.startup_config import StartupConfigs
from app.utilities import Commands, Utilities


# todo: add settings location directory set?

class Application(tk.Tk):
    tab_control: ttk.Notebook = None
    main_config: MainConfig = None
    alerts_config: AlertsConfig = None
    startup_config: StartupConfigs = None
    about: About = None
    output_console: OutputConsole = None
    commands: Commands = None

    def __init__(self, root_path):
        super().__init__()
        self.root_path: str = root_path
        self.initial_setup()
        self.settings_handler: SettingsHandler = SettingsHandler()
        Utilities.Utilities.set_application(self)
        self.create_subcomponents()
        self.commands = Commands.Commands(self)

        try:
            self.iconbitmap(os.path.join(self.root_path, 'palworld_logo.ico'))
        except Exception as e:
            self.append_output("Icon wasn't able to load due to error: " + str(e))
        self.load_settings()
        self.after(250, self.save())

    def initial_setup(self) -> None:
        self.tab_control: ttk.Notebook = ttk.Notebook(self)
        self.title("PalWorld Dedicated Server Manager")
        self.tab_control.pack(expand=1, fill="both")
        self.protocol("WM_DELETE_WINDOW", self.on_exit)

    def create_subcomponents(self) -> None:
        self.output_console: OutputConsole = OutputConsole.OutputConsole(self)
        self.main_config: MainConfig = MainConfig.MainConfig(self)
        self.startup_config: StartupConfigs = StartupConfigs.StartupConfigs(self)
        self.alerts_config: AlertsConfig = AlertsConfig.AlertsConfig(self)
        self.about: About = About.About(self)

    def update_commands(self):
        self.commands.update_commands()

    def save(self, one_off=False) -> None:
        """
        Gathers and writes the settings of all subordinate elements to the file
        """
        self.main_config.save()
        self.startup_config.save()
        self.alerts_config.save()
        self.settings_handler.save()
        if not one_off:
            self.after(5 * 1000, self.save)

    def on_exit(self) -> None:
        self.save(one_off=True)
        self.destroy()

    def load_settings(self) -> None:
        try:
            with open(self.settings_handler.settings_location.get(), "r") as file:
                self.settings_handler.restore(file)
        except FileNotFoundError:
            self.append_output("First time startup or errored config file. Applying default configuration")
        self.main_config.restore()
        self.startup_config.restore()
        self.alerts_config.restore()

    def get_tab_control(self) -> ttk.Notebook:
        return self.tab_control

    def append_output(self, message) -> None:
        self.output_console.append_output(message)

    def interval_restart_enabled(self):
        return self.main_config.interval_restart_enabled()

    def daily_restart_enabled(self):
        return self.main_config.daily_restart_enabled()

    def monitor_interval_enabled(self):
        return self.main_config.monitor_interval_enabled()

    def backup_interval_enabled(self):
        return self.main_config.backup_interval_enabled()

    def email_notification_enabled(self):
        return self.main_config.email_notification_enabled()

    def discord_notification_enabled(self):
        return self.main_config.discord_notification_enabled()

    def startup_update_check_enabled(self):
        return self.main_config.startup_update_check_enabled()

    def backup_during_restart_enabled(self):
        return self.main_config.backup_during_restart_enabled()

    def delete_old_backups_enabled(self):
        return self.main_config.delete_old_backups_enabled()
