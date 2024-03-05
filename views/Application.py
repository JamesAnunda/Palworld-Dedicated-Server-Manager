import json
import os
import tkinter as tk
from tkinter import ttk

from views import OutputConsole
from views.tabs.main import MainConfig
from views.tabs.server_config import StartupConfigs


class Application(tk.Tk):
    tab_control = None
    main_config: MainConfig = None
    alerts_config = None
    startup_config: StartupConfigs = None
    about = None
    output_console: OutputConsole = None

    def __init__(self):
        super().__init__()
        self.settings_file = os.path.join(os.path.expanduser("~"), "Documents/Palworld Server Manager", "settings.json")
        self.initial_setup()
        self.create_subcomponents()
        self.load_settings()

    def initial_setup(self):
        self.tab_control: ttk.Notebook = ttk.Notebook(self)
        self.title("Palworld Dedicated Server Manager")
        self.tab_control.pack(expand=1, fill="both")
        self.protocol("WM_DELETE_WINDOW", self.on_exit)

    def create_subcomponents(self):
        self.main_config = MainConfig.MainConfig(self)
        self.alerts_config = None  # todo
        self.startup_config = StartupConfigs.StartupConfigs(self)
        self.about = None  # todo
        self.output_console = OutputConsole.OutputConsole(self)

    def save(self):
        """
        Top-level save, does not return anything. Is not inherited. Just... is.

        Gathers and writes the settings of all subordinate elements to the file
        """
        settings_directory = os.path.join(os.path.expanduser("~"), "Documents/Palworld Server Manager")
        if not os.path.exists(settings_directory):
            os.makedirs(settings_directory)

        settings = self.main_config.save() | self.startup_config.save()  #| self.alerts_config.save() | self.about.save()
        with open(self.settings_file, "w") as file:
            json.dump(settings, file)

    def on_exit(self):
        self.save()
        self.destroy()

    def load_settings(self):
        try:
            with open(self.settings_file, "r") as file:
                settings = json.load(file)
                self.main_config.restore(settings)
                self.startup_config.restore(settings)
        except FileNotFoundError:
            pass
            # append_to_output("First time startup. Applying default configuration")
            # server_directory_selection.config(text="No directory selected", foreground="red")
            # arrcon_directory_selection.config(text="No directory selected", foreground="red")
            # steamcmd_directory_selection.config(text="No directory selected", foreground="red")
            # backup_directory_selection.config(text="No directory selected", foreground="red")
            # server_start_args_entry.insert(0, '-useperfthreads -NoAsyncLoadingThread -UseMultithreadForDS -EpicApp=PalServer')
            # smtp_server_entry.insert(0, "smtp.gmail.com")
            # smtp_port_entry.insert(0, "587")

    def get_tab_control(self):
        return self.tab_control


if __name__ == "__main__":
    app = Application()
    app.mainloop()
