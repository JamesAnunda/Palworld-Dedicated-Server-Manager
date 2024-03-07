import tkinter as tk
from tkinter import ttk

from app.handlers import SettingsHandler
from app.tabs.alerts_config import AlertsConfig
from app.utilities import TkViewElements, Utilities
from app.utilities.StateInterfaces import IRestorable, ISavable


class DiscordConfig(TkViewElements.TkLabelFrame, ISavable, IRestorable):
    def __init__(self, alerts_config: 'AlertsConfig.AlertsConfig', settings_handler: 'SettingsHandler.SettingsHandler', label_text: str = "Discord Config", column: int = 1, row: int = 0, sticky: tk.constants = tk.NSEW):
        super().__init__(alerts_config, label_text, column, row, sticky)
        self.settings_handler: SettingsHandler = settings_handler

        row = 0
        ttk.Label(self, text="Discord Webhook URL:").grid(column=0, row=row, padx=10, sticky=tk.W)
        self.discord_webhook = tk.StringVar()
        ttk.Entry(self, textvariable=self.discord_webhook, width=35).grid(column=1, row=row)

        row += 1
        ttk.Button(self, text="Send Test Message", command=Utilities.send_discord_message).grid(column=1, row=row, columnspan=2, pady=2)

    def save(self) -> None:
        self.settings_handler.discord_webhook.set(self.discord_webhook.get())

    def restore(self) -> None:
        self.discord_webhook.set(self.settings_handler.discord_webhook.get())
