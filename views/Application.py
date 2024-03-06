import json
import os
import tkinter as tk
from tkinter import ttk

from utilities.Constants import SaveSettings
from views import OutputConsole
from views.tabs.about import About
from views.tabs.alerts_config import AlertsConfig
from views.tabs.main import MainConfig
from views.tabs.server_config import StartupConfigs


class Application(tk.Tk):
    tab_control: ttk.Notebook = None
    main_config: MainConfig = None
    alerts_config: AlertsConfig = None
    startup_config: StartupConfigs = None
    about: About = None
    output_console: OutputConsole = None

    def __init__(self, root_path):
        super().__init__()
        self.root_path: str = root_path
        settings_directory: str = os.path.join(os.path.expanduser("~"), "Documents/Palworld Server Manager")
        if not os.path.exists(settings_directory):
            os.makedirs(settings_directory)
        self.settings_file: str = os.path.join(os.path.expanduser("~"), "Documents/Palworld Server Manager", "settings.json")
        self.initial_setup()
        self.create_subcomponents()

        ttk.Style().theme_use('winnative')
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
        self.main_config: MainConfig = MainConfig.MainConfig(self)
        self.startup_config: StartupConfigs = StartupConfigs.StartupConfigs(self)
        self.alerts_config: AlertsConfig = AlertsConfig.AlertsConfig(self)
        self.about: About = About.About(self)
        self.output_console: OutputConsole = OutputConsole.OutputConsole(self)

    def save(self) -> None:
        """
        Gathers and writes the settings of all subordinate elements to the file
        """
        settings = self.main_config.save() | self.startup_config.save()  #| self.alerts_config.save()
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
        except FileNotFoundError:
            pass
            self.append_output("First time startup or errored config file. Applying default configuration")
            self.startup_config.server_configs.palworld_dir.set(SaveSettings.palworld_directory_default)
            # server_directory_selection.config(text="No directory selected", foreground="red")
            # arrcon_directory_selection.config(text="No directory selected", foreground="red")
            # steamcmd_directory_selection.config(text="No directory selected", foreground="red")
            # backup_directory_selection.config(text="No directory selected", foreground="red")
            # server_start_args_entry.insert(0, '-useperfthreads -NoAsyncLoadingThread -UseMultithreadForDS -EpicApp=PalServer')
            # smtp_server_entry.insert(0, "smtp.gmail.com")
            # smtp_port_entry.insert(0, "587")

    def get_tab_control(self) -> ttk.Notebook:
        return self.tab_control

    def append_output(self, message) -> None:
        self.output_console.append_output(message)
