import tkinter as tk
from tkinter import ttk

from app.tabs.alerts_config import AlertsConfig
from app.utilities import TkViewElements, Utilities
from app.utilities.Constants import SaveSettings
from app.utilities.StateInterfaces import IRestorable, ISavable
from app.utilities.Utilities import get_or_default


class EmailConfig(TkViewElements.TkLabelFrame, ISavable, IRestorable):
    def __init__(self, alerts_config: 'AlertsConfig.AlertsConfig', label_text: str = "Email Config", column: int = 0, row: int = 0, sticky: tk.constants = tk.NSEW):
        super().__init__(alerts_config, label_text, column, row, sticky)

        self.email_address = tk.StringVar()
        self.email_password = tk.StringVar()
        self.smtp_server = tk.StringVar()
        self.smtp_port = tk.StringVar()

        row = 0
        ttk.Label(self, text="Email Address:").grid(column=0, row=0, padx=10, sticky=tk.W)
        ttk.Entry(self, textvariable=self.email_address, width=35).grid(column=1, row=row, sticky=tk.W)

        row += 1
        ttk.Label(self, text="Email Password*:").grid(column=0, row=row, padx=10, sticky=tk.W)
        self.email_password_entry = ttk.Entry(self, textvariable=self.email_password, show="*", width=35)
        self.email_password_entry.grid(column=1, row=row, sticky=tk.W)
        self.show_password_btn = ttk.Button(self, text="Show Pass", command=self.show_password)
        self.show_password_btn.grid(column=2, row=row, sticky=tk.W)

        row += 1
        ttk.Label(self, text="SMTP Server:").grid(column=0, row=2, padx=10, sticky=tk.W)
        ttk.Entry(self, textvariable=self.smtp_server, width=35).grid(column=1, row=row, sticky=tk.W)

        row += 1
        ttk.Label(self, text="SMTP Port:").grid(column=0, row=row, padx=10, sticky=tk.W)
        ttk.Entry(self, textvariable=self.smtp_port, width=5).grid(column=1, row=row, sticky=tk.W)

        row += 1
        ttk.Button(self, text="Send Test Email", command=Utilities.send_test_email).grid(column=1, row=row, columnspan=3, sticky=tk.S)

        row += 1
        ttk.Label(self, text="* Password is NOT saved, needs to be put in every Manager restart").grid(column=0, row=row, columnspan=3, sticky=tk.W)

    def save(self) -> dict:
        return {
                SaveSettings.email_address: get_or_default(self.email_address.get(), SaveSettings.email_address_default),
                SaveSettings.smtp_server:   get_or_default(self.smtp_server.get(), SaveSettings.smtp_server),
                SaveSettings.smtp_port:     get_or_default(self.smtp_port.get(), SaveSettings.smtp_port_default)
        }

    def restore(self, restore_data: dict) -> None:
        self.email_address.set(restore_data.get(SaveSettings.email_address, SaveSettings.email_address_default))
        self.smtp_server.set(restore_data.get(SaveSettings.smtp_server, SaveSettings.smtp_server_default))
        self.smtp_port.set(restore_data.get(SaveSettings.smtp_port, SaveSettings.smtp_port_default))

    def show_password(self):
        (show, text) = ('*', 'Show Pass') if self.email_password_entry.cget('show') == '' else ('', 'Hide Pass')
        self.email_password_entry.config(show=show)
        self.show_password_btn.config(text=text)
