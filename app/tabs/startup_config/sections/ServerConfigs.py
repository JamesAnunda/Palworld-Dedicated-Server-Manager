import tkinter as tk
from tkinter import ttk

from app.tabs.startup_config import StartupConfigs
from app.utilities import TkViewElements
from app.utilities.Constants import SaveSettings
from app.utilities.StateInterfaces import IRestorable, ISavable
from app.utilities.Utilities import get_or_default


class ServerConfigs(TkViewElements.TkLabelFrame, ISavable, IRestorable):
    def __init__(self, startup_configs: 'StartupConfigs.StartupConfigs', label_text: str = "Server Configuration", column: int = 0, row: int = 1, sticky: tk.constants = tk.S):
        super().__init__(startup_configs, label_text, column, row, sticky)
        self.startup_configs: StartupConfigs = startup_configs

        row = 0
        self.palworld_dir = tk.StringVar(value=SaveSettings.palworld_directory_default)
        self.create_dir_search("Select PalWorld Directory", self.palworld_dir, None, row)
        self.pal_status_label = tk.Label(self, text="Status Unknown", width=30)
        self.pal_status_label.grid(column=2, row=row, sticky=tk.E, padx=10, pady=10)

        row += 1
        self.arrcon_dir = tk.StringVar(value=SaveSettings.arrcon_directory_default)
        self.create_dir_search("Select ARRCON Directory", self.arrcon_dir, None, row)
        self.arrcon_status_label = tk.Label(self, text="Status Unknown", width=30)
        self.arrcon_status_label.grid(column=2, row=row, sticky=tk.E, padx=10, pady=10)

        row += 1
        self.steamcmd_dir = tk.StringVar(value=SaveSettings.steamcmd_directory_default)
        self.create_dir_search("Select SteamCmd Directory", self.steamcmd_dir, None, row)
        self.steamcmd_status_label = tk.Label(self, text="Status Unknown", width=30)
        self.steamcmd_status_label.grid(column=2, row=row, sticky=tk.E, padx=10, pady=10)

        row += 1
        self.backup_dir = tk.StringVar(value=SaveSettings.backup_directory_default)
        self.create_dir_search("Select Backup Directory", self.backup_dir, None, 3)

        row += 1
        self.server_start_args = tk.StringVar(value=SaveSettings.server_start_args_default)
        ttk.Label(self, text="Server Startup Args: ").grid(column=0, row=row, padx=10, pady=10, sticky=tk.N)
        ttk.Entry(self, textvariable=self.server_start_args, width=100).grid(column=1, row=row, columnspan=2, padx=10, pady=10, sticky=tk.W)

    def save(self) -> dict:
        return {
                SaveSettings.palworld_directory: get_or_default(self.palworld_dir.get(), SaveSettings.palworld_directory_default),
                SaveSettings.arrcon_directory:   get_or_default(self.arrcon_dir.get(), SaveSettings.arrcon_directory_default),
                SaveSettings.steamcmd_directory: get_or_default(self.steamcmd_dir.get(), SaveSettings.steamcmd_directory_default),
                SaveSettings.backup_directory:   get_or_default(self.backup_dir.get(), SaveSettings.backup_directory_default),
                SaveSettings.server_start_args:  get_or_default(self.server_start_args.get(), SaveSettings.server_start_args_default),
        }

    def restore(self, restore_data: dict) -> None:
        self.palworld_dir.set(restore_data.get(SaveSettings.palworld_directory, SaveSettings.palworld_directory_default))
        self.arrcon_dir.set(restore_data.get(SaveSettings.arrcon_directory, SaveSettings.arrcon_directory_default))
        self.steamcmd_dir.set(restore_data.get(SaveSettings.steamcmd_directory, SaveSettings.steamcmd_directory_default))
        self.backup_dir.set(restore_data.get(SaveSettings.backup_directory, SaveSettings.backup_directory_default))

    def append_output(self, message) -> None:
        self.startup_configs.append_output(message)

    def create_dir_search(self, btn_txt, dir_var, command, row) -> None:
        ttk.Button(self, text=btn_txt, command=command, width=30).grid(column=0, row=row, sticky=tk.W, padx=10, pady=10)
        ttk.Label(self, textvariable=dir_var).grid(column=1, row=row, sticky=tk.W, padx=10, pady=10)

    def update_statuses(self) -> None:
        pass
