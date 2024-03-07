import tkinter as tk
from tkinter import ttk

from app.tabs.alerts_config import AlertsConfig
from app.utilities import TkViewElements, Utilities
from app.utilities.Constants import SaveSettings
from app.utilities.StateInterfaces import IRestorable, ISavable
from app.utilities.Utilities import get_or_default


class DiscordConfig(TkViewElements.TkLabelFrame, ISavable, IRestorable):
    def __init__(self, alerts_config: 'AlertsConfig.AlertsConfig', label_text: str = "Discord Config", column: int = 1, row: int = 0, sticky: tk.constants = tk.NSEW):
        super().__init__(alerts_config, label_text, column, row, sticky)

        row = 0
        ttk.Label(self, text="Discord Webhook URL:").grid(column=0, row=row, padx=10, sticky=tk.W)
        self.discord_webhook = tk.StringVar()
        ttk.Entry(self, textvariable=self.discord_webhook, width=35).grid(column=1, row=row)

        row += 1
        ttk.Button(self, text="Send Test Message", command=Utilities.send_discord_message).grid(column=1, row=row, columnspan=2, pady=2)

    def save(self) -> dict:
        return {
                SaveSettings.discord_webhook: get_or_default(self.discord_webhook.get(), SaveSettings.discord_webhook_default)
        }

    def restore(self, restore_data: dict) -> None:
        self.discord_webhook.set(restore_data.get(SaveSettings.discord_webhook, SaveSettings.discord_webhook_default))
