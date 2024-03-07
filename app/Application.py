import json
import os
import tkinter as tk
from tkinter import ttk

from app import OutputConsole
from app.tabs.about import About
from app.tabs.alerts_config import AlertsConfig
from app.tabs.main import MainConfig
from app.tabs.startup_config import StartupConfigs
from app.utilities import Commands
from app.utilities.Constants import SaveSettings


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
        settings_directory: str = os.path.join(os.path.expanduser("~"), "Documents\\Palworld Server Manager")
        if not os.path.exists(settings_directory):
            os.makedirs(settings_directory)
        self.settings_file: str = os.path.join(os.path.expanduser("~"), "Documents\\Palworld Server Manager", "settings.json")
        self.initial_setup()
        self.create_subcomponents()

        try:
            self.iconbitmap(os.path.join(self.root_path, 'palworld_logo.ico'))
        except Exception as e:
            self.append_output("Icon wasn't able to load due to error: " + str(e))
        self.load_settings()

    def initial_setup(self) -> None:
        self.tab_control: ttk.Notebook = ttk.Notebook(self)
        self.title("Palworld Dedicated Server Manager")
        self.tab_control.pack(expand=1, fill="both")
        self.protocol("WM_DELETE_WINDOW", self.on_exit)

    def create_subcomponents(self) -> None:
        self.output_console: OutputConsole = OutputConsole.OutputConsole(self)
        self.main_config: MainConfig = MainConfig.MainConfig(self)
        self.startup_config: StartupConfigs = StartupConfigs.StartupConfigs(self)
        self.alerts_config: AlertsConfig = AlertsConfig.AlertsConfig(self)
        self.about: About = About.About(self)

    def initialize_commands(self):
        self.commands = Commands.Commands(self)

    def save(self) -> None:
        """
        Gathers and writes the settings of all subordinate elements to the file
        """
        settings = self.main_config.save() | self.startup_config.save() | self.alerts_config.save()
        with open(self.settings_file, "w") as file:
            json.dump(settings, file)

    def on_exit(self) -> None:
        self.save()
        self.destroy()

    def load_settings(self) -> None:
        try:
            with open(self.settings_file, "r") as file:
                settings = json.load(file)
                self.main_config.restore(settings)
                self.startup_config.restore(settings)
                self.alerts_config.restore(settings)
        except FileNotFoundError:
            pass
            self.append_output("First time startup or errored config file. Applying default configuration")
            self.startup_config.restore({
                    SaveSettings.palworld_directory: SaveSettings.palworld_directory_default,
                    SaveSettings.server_start_args:  SaveSettings.server_start_args_default
            })
            self.alerts_config.restore({
                    SaveSettings.smtp_server: SaveSettings.smtp_server_default,
                    SaveSettings.smtp_port:   SaveSettings.smtp_port_default
            })

    def get_tab_control(self) -> ttk.Notebook:
        return self.tab_control

    def append_output(self, message) -> None:
        self.output_console.append_output(message)
