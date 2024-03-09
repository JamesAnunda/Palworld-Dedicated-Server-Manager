import os.path
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename

from app.handlers import SettingsHandler
from app.tabs.startup_config import StartupConfigs
from app.utilities import TkViewElements
from app.utilities.StateInterfaces import IRestorable, ISavable


class ServerConfigs(TkViewElements.TkLabelFrame, ISavable, IRestorable):
    def __init__(self, startup_configs: 'StartupConfigs.StartupConfigs', settings_handler: 'SettingsHandler.SettingsHandler', label_text: str = "Server Configuration", column: int = 0, row: int = 1, sticky: tk.constants = tk.S):
        super().__init__(startup_configs, label_text, column, row, sticky)
        self.startup_configs: StartupConfigs = startup_configs
        self.settings_handler: SettingsHandler = settings_handler

        row = 0
        self.palworld_dir = tk.StringVar(value=self.settings_handler.palworld_location.get())
        self.create_dir_search("Select PalWorld Directory", self.palworld_dir, row)
        self.pal_status_label = tk.Label(self, text="Status Unknown", width=30)
        self.pal_status_label.grid(column=2, row=row, sticky=tk.E, padx=10, pady=10)

        row += 1
        self.arrcon_dir = tk.StringVar(value=self.settings_handler.arrcon_location.get())
        self.create_dir_search("Select ARRCON Directory", self.arrcon_dir, row)
        self.arrcon_status_label = tk.Label(self, text="Status Unknown", width=30)
        self.arrcon_status_label.grid(column=2, row=row, sticky=tk.E, padx=10, pady=10)

        row += 1
        self.steamcmd_dir = tk.StringVar(value=self.settings_handler.steamcmd_location.get())
        self.create_dir_search("Select SteamCmd Directory", self.steamcmd_dir, row)
        self.steamcmd_status_label = tk.Label(self, text="Status Unknown", width=30)
        self.steamcmd_status_label.grid(column=2, row=row, sticky=tk.E, padx=10, pady=10)

        row += 1
        self.backup_dir = tk.StringVar(value=self.settings_handler.backup_location.get())
        self.create_dir_search("Select Backup Directory", self.backup_dir, 3, backup=True)

        row += 1
        self.server_start_args = tk.StringVar(value=self.settings_handler.server_start_args.get())
        ttk.Label(self, text="Server Startup Args: ").grid(column=0, row=row, padx=10, pady=10, sticky=tk.N)
        ttk.Entry(self, textvariable=self.server_start_args, width=100).grid(column=1, row=row, columnspan=2, padx=10, pady=10, sticky=tk.W)

    def save(self) -> None:
        self.settings_handler.palworld_location.set(self.palworld_dir.get())
        self.settings_handler.arrcon_location.set(self.arrcon_dir.get())
        self.settings_handler.steamcmd_location.set(self.steamcmd_dir.get())
        self.settings_handler.backup_location.set(self.backup_dir.get())
        self.settings_handler.server_start_args.set(self.server_start_args.get())

    def restore(self) -> None:
        self.palworld_dir.set(self.settings_handler.palworld_location.get())
        self.arrcon_dir.set(self.settings_handler.arrcon_location.get())
        self.steamcmd_dir.set(self.settings_handler.steamcmd_location.get())
        self.backup_dir.set(self.settings_handler.backup_location.get())
        self.update_statuses()

    def append_output(self, message) -> None:
        self.startup_configs.append_output(message)

    def create_dir_search(self, btn_txt, dir_var, row, backup=False) -> None:
        ttk.Button(self, text=btn_txt, command=lambda: self.get_directory(dir_var, backup), width=30).grid(column=0, row=row, sticky=tk.W, padx=10, pady=10)
        ttk.Label(self, textvariable=dir_var).grid(column=1, row=row, sticky=tk.W, padx=10, pady=10)

    def update_statuses(self) -> None:
        self.__update_status_helper(self.palworld_dir.get(), "PalServer.exe", self.pal_status_label)
        self.__update_status_helper(self.arrcon_dir.get(), "ARRCON.exe", self.arrcon_status_label)
        self.__update_status_helper(self.steamcmd_dir.get(), "steamcmd.exe", self.steamcmd_status_label)

    def __update_status_helper(self, directory, exe, label):
        if os.path.exists(directory) and os.path.exists(os.path.join(directory, exe)):
            label.configure(text="Exe Found!", background="SystemButtonFace", foreground="green")
            self.append_output(exe.title() + " found!")
        else:
            label.configure(text="Exe NOT Found...", background="black", foreground="red")
            self.append_output(exe + " not found, please install and select the appropriate directory.")

    def get_directory(self, var, backup=False):
        temp = tk.filedialog.askopenfilename() if not backup else tk.filedialog.askdirectory()
        if temp is None or temp == "":
            return
        var.set(os.path.dirname(temp) if not os.path.isdir(temp) else temp)
        self.startup_configs.application.save()
        self.update_statuses()
