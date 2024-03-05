import tkinter as tk
from tkinter import ttk

from utilities import TkViewElements
from views.tabs.main import MainConfig


class ServerInfo(TkViewElements.TkLabelFrame):

    def __init__(self, main_config: 'MainConfig.MainConfig', label_text: str = "Server Info", column: int = 1, row: int = 0, sticky: tk.constants = tk.NSEW):
        super().__init__(main_config, label_text, column, row, sticky)
        self.main_config = main_config

        row = 0

        self.server_status_bool = tk.BooleanVar()
        self.server_status_str = tk.StringVar(value="?")
        ttk.Label(self, text="Server Status: ", anchor="w").grid(column=0, row=row, sticky=tk.W)
        self.server_status_label = ttk.Label(self, textvariable=self.server_status_str, anchor="e")
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

    def update_server_status_label(self):
        if self.server_status_bool.get():
            self.server_status_str.set("Online")
            self.server_status_label.config(foreground="green")
        else:
            self.server_status_str.set("OFFLINE")
            self.server_status_label.config(foreground="black", background="red")

    def update_server_status(self):
        pass

    def update_server_version(self):
        pass

    def update_server_info(self):
        self.update_server_status_label()
        self.update_server_status()
        self.update_server_version()
