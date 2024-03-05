import tkinter as tk
from tkinter import ttk

import requests

from utilities import TkViewElements, Utilities
from utilities.Constants import SaveSettings
from utilities.StateInterfaces import IRestorable, ISavable
from views.tabs.main import MainConfig


class ServerInfo(TkViewElements.TkLabelFrame, ISavable, IRestorable):
    update_after_id = None  # keeps track of update threads, will cancel existing one if new thread is created before it's finished

    def __init__(self, main_config: 'MainConfig.MainConfig', label_text: str = "Server Info", column: int = 1, row: int = 0, sticky: tk.constants = tk.NSEW):
        super().__init__(main_config, label_text, column, row, sticky)
        self.main_config = main_config

        row = 0

        self.server_status_bool = tk.BooleanVar()
        self.server_status_str = tk.StringVar(value="?")
        ttk.Label(self, text="Server Status: ", anchor="w").grid(column=0, row=row, sticky=tk.W)
        self.server_status_label = tk.Label(self, textvariable=self.server_status_str, anchor="e")
        self.server_status_label.grid(column=1, row=row, sticky=tk.E)

        row += 1

        self.server_version_str = tk.StringVar(value="?")
        ttk.Label(self, text="Server Version: ", anchor="w").grid(column=0, row=row, sticky=tk.W)
        ttk.Label(self, textvariable=self.server_version_str, anchor="e").grid(column=1, row=row, sticky=tk.E)

        row += 1

        self.external_ip = tk.StringVar(value="?")
        ttk.Label(self, text="External IP: ", anchor="w").grid(column=0, row=row, sticky=tk.W)
        ttk.Label(self, textvariable=self.external_ip, width=16, anchor="e").grid(column=1, row=row, sticky=tk.E)

        row += 1

        ttk.Button(self, text="Update Now", command=self.update_server_info).grid(column=0, row=row, columnspan=2, sticky=tk.S)

    def save(self) -> dict:
        return {
                SaveSettings.external_ip: Utilities.get_or_default(self.external_ip.get(), SaveSettings.external_ip_default)
        }

    def restore(self, restore_data: dict) -> None:
        self.external_ip.set(restore_data.get(SaveSettings.external_ip, SaveSettings.external_ip_default))

    def update_server_status_label(self):
        if self.server_status_bool.get():
            self.server_status_str.set("Online")
            self.server_status_label.config(foreground="green", background="SystemButtonFace")  # this is the default tk background color
        else:
            self.server_status_str.set("OFFLINE")
            (fg, bg) = ("black", "red") if self.server_status_label.cget("foreground") == "red" else ("red", "black")
            self.server_status_label.configure(activeforeground=fg, foreground=fg, activebackground=bg, background=bg)

    def update_server_version(self):
        pass

    def update_external_ip(self):
        ip_response = requests.get('https://api.ipify.org').text
        if ip_response != self.external_ip.get():
            self.append_output("External IP address change detected")
            self.external_ip.set(ip_response)
            # todo - send discord message on change

    def update_server_info(self):
        self.update_server_status_label()
        self.update_server_version()
        self.update_external_ip()
        self.update_after_id = self.after_cancel(self.update_after_id) if self.update_after_id is not None else None
        self.update_after_id = self.after(1000, lambda: self.update_server_info())

    def append_output(self, message):
        self.main_config.append_output(message)
