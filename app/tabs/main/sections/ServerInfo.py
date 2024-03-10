import tkinter as tk
from tkinter import ttk

import requests

from app.handlers import SettingsHandler
from app.tabs.main import MainConfig
from app.utilities import TkViewElements
from app.utilities.StateInterfaces import IRestorable, ISavable
from app.utilities.Utilities import MessageLevel, Utilities


class ServerInfo(TkViewElements.TkLabelFrame, ISavable, IRestorable):
    update_after_id: str | None = None  # keeps track of update threads, will cancel existing one if new thread is created before it's finished

    def __init__(self, main_config: 'MainConfig.MainConfig', settings_handler: 'SettingsHandler.SettingsHandler', label_text: str = "Server Info", column: int = 1, row: int = 0, sticky: tk.constants = tk.NSEW):
        super().__init__(main_config, label_text, column, row, sticky)
        self.main_config: MainConfig = main_config
        self.settings_handler: SettingsHandler = settings_handler

        row = 0
        self.server_status_bool = tk.BooleanVar()
        self.server_status = tk.StringVar(value="?")
        ttk.Label(self, text="Server Status: ", anchor="w").grid(column=0, row=row, sticky=tk.W)
        self.server_status_label = tk.Label(self, textvariable=self.server_status, anchor="e")
        self.server_status_label.grid(column=1, row=row, sticky=tk.E)

        row += 1
        self.server_version = tk.StringVar(value="?")
        ttk.Label(self, text="Server Version: ", anchor="w").grid(column=0, row=row, sticky=tk.W)
        ttk.Label(self, textvariable=self.server_version, anchor="e").grid(column=1, row=row, sticky=tk.E)

        row += 1
        self.external_ip = tk.StringVar()
        ttk.Label(self, text="External IP: ", anchor="w").grid(column=0, row=row, sticky=tk.W)
        ttk.Label(self, textvariable=self.external_ip, width=16, anchor="e").grid(column=1, row=row, sticky=tk.E)

        row += 1
        ttk.Button(self, text="Update Now", command=self.update_server_info).grid(column=1, row=row, sticky=tk.E)

    def save(self) -> None:
        self.settings_handler.external_ip.set(self.external_ip.get())

    def restore(self) -> None:
        self.external_ip.set(self.settings_handler.external_ip.get())

    def update_server_status(self):
        """
        Update self.server_status_bool to the current running state
        """
        pass

    def update_server_status_label(self) -> None:
        if self.server_status_bool.get():
            self.server_status.set("Online")
            self.server_status_label.config(foreground="green", background="SystemButtonFace")  # this is the default tk background color
        else:
            self.server_status.set("OFFLINE")
            (fg, bg) = ("black", "red") if self.server_status_label.cget("foreground") == "red" else ("red", "black")
            self.server_status_label.configure(activeforeground=fg, foreground=fg, activebackground=bg, background=bg)

    def update_server_version(self) -> None:
        if self.server_status_bool.get():
            pass
        else:
            self.server_version.set("?")
        # todo: update server version label from runtime as server starts, check if is up to date version?
        #  add button to get latest Palserver version?
        pass

    def update_external_ip(self) -> None:
        ip_response = requests.get('https://api.ipify.org').text
        if ip_response != self.external_ip.get():
            self.append_output("External IP address change detected")
            self.external_ip.set(ip_response)
            Utilities.send_discord_message(f"The server IP has changed to {self.external_ip.get()}, please update your connections on next startup!",
                                           MessageLevel.PLAYER_ACTION_REQUIRED)
            # todo does ip roll cause issues during runtime?
            # close server
            # update ini w/ new ip
            # restart server

    def update_server_info(self) -> None:
        self.update_server_status()
        self.update_server_version()
        self.update_external_ip()
        self.update_server_status_label()
        self.update_after_id = self.after_cancel(self.update_after_id) if self.update_after_id is not None else None
        self.update_after_id = self.after(1000, lambda: self.update_server_info())

    def append_output(self, message) -> None:
        self.main_config.append_output(message)
