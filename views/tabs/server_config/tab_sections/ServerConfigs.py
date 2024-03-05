import tkinter as tk
from tkinter import ttk

from utilities import TkViewElements
from utilities.Constants import SaveSettings
from utilities.StateInterfaces import IRestorable, ISavable
from utilities.Utilities import get_or_default
from views.tabs.server_config import StartupConfigs


class ServerConfigs(TkViewElements.TkLabelFrame, ISavable, IRestorable):

    def __init__(self, startup_configs: 'StartupConfigs.StartupConfigs', label_text: str = "Server Configuration", column: int = 0, row: int = 1, sticky: tk.constants = tk.S):
        super().__init__(startup_configs, label_text, column, row, sticky)
        self.startup_configs: StartupConfigs = startup_configs

        row = 0
        self.palworld_dir_str = tk.StringVar(value=SaveSettings.palworld_directory_default)
        self.create_dir_search("Select PalWorld Directory", self.palworld_dir_str, None, row)
        self.pal_status_label = tk.Label(self, text="Status Unknown", width=30)
        self.pal_status_label.grid(column=2, row=row, sticky=tk.E, padx=10, pady=10)

        row += 1
        self.arrcon_dir_str = tk.StringVar(value=SaveSettings.arrcon_directory_default)
        self.create_dir_search("Select ARRCON Directory", self.arrcon_dir_str, None, row)
        self.arrcon_status_label = tk.Label(self, text="Status Unknown", width=30)
        self.arrcon_status_label.grid(column=2, row=row, sticky=tk.E, padx=10, pady=10)

        row += 1
        self.steamcmd_dir_str = tk.StringVar(value=SaveSettings.steamcmd_directory_default)
        self.create_dir_search("Select SteamCmd Directory", self.steamcmd_dir_str, None, row)
        self.steamcmd_status_label = tk.Label(self, text="Status Unknown", width=30)
        self.steamcmd_status_label.grid(column=2, row=row, sticky=tk.E, padx=10, pady=10)

        row += 1
        self.backup_dir_str = tk.StringVar(value=SaveSettings.backup_directory_default)
        self.create_dir_search("Select Backup Directory", self.backup_dir_str, None, 3)

        row += 1
        self.server_start_args = tk.StringVar(value=SaveSettings.server_start_args_default)
        ttk.Label(self, text="Server Startup Args: ").grid(column=0, row=row, sticky=tk.N)
        ttk.Entry(self, textvariable=self.server_start_args, width=100).grid(column=1, row=row, columnspan=2, sticky=tk.NSEW)

    def save(self) -> dict:
        return {
                SaveSettings.palworld_directory: get_or_default(self.palworld_dir_str.get(), SaveSettings.palworld_directory_default),
                SaveSettings.arrcon_directory:   get_or_default(self.arrcon_dir_str.get(), SaveSettings.arrcon_directory_default),
                SaveSettings.steamcmd_directory: get_or_default(self.steamcmd_dir_str.get(), SaveSettings.steamcmd_directory_default),
                SaveSettings.backup_directory:   get_or_default(self.backup_dir_str.get(), SaveSettings.backup_directory_default),
                SaveSettings.server_start_args:  get_or_default(self.server_start_args.get(), SaveSettings.server_start_args_default),
        }

    def restore(self, restore_data: dict) -> None:
        self.palworld_dir_str.set(restore_data.get(SaveSettings.palworld_directory, SaveSettings.palworld_directory_default))
        self.arrcon_dir_str.set(restore_data.get(SaveSettings.arrcon_directory, SaveSettings.arrcon_directory_default))
        self.steamcmd_dir_str.set(restore_data.get(SaveSettings.steamcmd_directory, SaveSettings.steamcmd_directory_default))
        self.backup_dir_str.set(restore_data.get(SaveSettings.backup_directory, SaveSettings.backup_directory_default))

    def create_dir_search(self, btn_txt, dir_var, command, row):
        ttk.Button(self, text=btn_txt, command=command, width=30).grid(column=0, row=row, sticky=tk.W, padx=10, pady=10)
        ttk.Label(self, textvariable=dir_var, width=75).grid(column=1, row=row, sticky=tk.W, padx=10, pady=10)

    def update_statuses(self):
        pass
