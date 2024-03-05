import tkinter as tk
from tkinter import ttk

from utilities import TkViewElements
from utilities.StateInterfaces import IRestorable
from views.tabs.server_config import StartupConfigs


class PalWorldSettings(TkViewElements.TkLabelFrame, IRestorable):

    def __init__(self, startup_configs: 'StartupConfigs.StartupConfigs', label_text: str = "PalWorldSettings.ini", column: int = 0, row: int = 0, sticky: tk.constants = tk.constants.N):
        super().__init__(startup_configs, label_text, column, row, sticky)
        self.startup_configs: StartupConfigs = startup_configs

        self.server_name = tk.StringVar(value="-")
        self.server_desc = tk.StringVar(value="-")
        self.server_pass = tk.StringVar(value="-")
        self.max_players = tk.StringVar(value="-")
        self.server_port = tk.StringVar(value="-")
        self.rcon_port = tk.StringVar(value="-")
        self.rcon_enabled = tk.StringVar(value="-")
        self.rcon_pass = tk.StringVar(value="-")

        self.create_setting_view("Server Name:", self.server_name, 0, 0)
        self.create_setting_view("Server Description:", self.server_desc, 0, 2)
        self.create_setting_view("Server Password:", self.server_pass, 0, 4)
        self.create_setting_view("Max Players:", self.max_players, 1, 0)
        self.create_setting_view("Server Port:", self.server_port, 1, 2)
        self.create_setting_view("RCON Port:", self.rcon_port, 2, 0)
        self.create_setting_view("RCON Enabled:", self.rcon_enabled, 2, 2)
        self.create_setting_view("RCON Password:", self.rcon_pass, 2, 4)

        ttk.Button(self, text="Edit PalWorldSettings.ini", command=self.open_palworld_settings).grid(column=0, row=7, columnspan=3)

    def restore(self, restore_data: dict) -> None:
        self.update_settings()

    def append_output(self, message):
        self.startup_configs.append_output(message)

    def create_setting_view(self, label_text, var, column, row):
        ttk.Label(self, text=label_text).grid(column=column, row=row, padx=10, sticky=tk.W)
        ttk.Label(self, textvariable=var).grid(column=column, row=row+1, padx=10, sticky=tk.W)

    def update_settings(self):
        pass

    def open_palworld_settings(self):
        pass
