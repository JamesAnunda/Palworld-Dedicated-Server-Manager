import tkinter as tk
from tkinter import ttk

from utilities import TkViewElements
from utilities.Constants import SaveSettings
from utilities.StateInterfaces import IRestorable, ISavable
from utilities.Utilities import get_or_default
from utilities.ValidationMethods import numeric_validate
from views.tabs.main import MainConfig


class OptionalConfig(TkViewElements.TkLabelFrame, ISavable, IRestorable):
    """
        Last level of UI elements, directly creates the visual items

        Specifically, handles all things regarding notifications and backup management
    """

    def __init__(self, main_config: 'MainConfig.MainConfig', label_text: str = "Optional Configs", column: int = 0, row: int = 1, sticky: tk.constants = tk.NSEW):
        super().__init__(main_config, label_text, column, row, sticky)
        self.main_config: MainConfig = main_config

        row = 0

        self.send_email_bool = tk.BooleanVar(value=False)
        ttk.Checkbutton(self, variable=self.send_email_bool, command=None).grid(column=0, row=row, sticky=tk.W)  # todo enable_send_email
        ttk.Label(self, text="Send Notification Email on Crash").grid(column=1, row=row, sticky=tk.W)

        row += 1

        self.send_discord_bool = tk.BooleanVar(value=False)
        ttk.Checkbutton(self, variable=self.send_discord_bool, command=None).grid(column=0, row=row, sticky=tk.W)  # todo enable_send_discord
        ttk.Label(self, text="Send Discord Channel Message on Crash").grid(column=1, row=row, sticky=tk.W)

        row += 1

        self.check_update_startup_bool = tk.BooleanVar(value=False)
        ttk.Checkbutton(self, variable=self.check_update_startup_bool, command=None).grid(column=0, row=row, sticky=tk.W)  # todo enable_check_for_updates
        ttk.Label(self, text="Check for Server Updates on Startup").grid(column=1, row=row, sticky=tk.W)

        row += 1

        self.backup_restart_bool = tk.BooleanVar(value=False)
        ttk.Checkbutton(self, variable=self.backup_restart_bool, command=None).grid(column=0, row=row, sticky=tk.W)  # todo enable_backup_on_restart
        ttk.Label(self, text="Backup Server during Restarts").grid(column=1, row=row, sticky=tk.W)

        row += 1

        self.delete_old_backups = tk.BooleanVar(value=False)
        self.delete_old_backups_days = tk.StringVar()
        ttk.Checkbutton(self, variable=self.delete_old_backups, command=None).grid(column=0, row=row, sticky=tk.W)  # todo enable_delete_backups
        ttk.Label(self, text="Backup Server during Restarts").grid(column=1, row=row, sticky=tk.W)
        ttk.Entry(self, textvariable=self.delete_old_backups_days, width=3, validate="key", validatecommand=(self.register(numeric_validate), '%P', '%d', 1, 365)).grid(column=2, row=row, sticky=tk.W)

        row += 1

    def save(self) -> dict:
        return {
                SaveSettings.delete_old_backups_days: get_or_default(self.delete_old_backups_days.get(), SaveSettings.delete_old_backups_days_default),
        }

    def restore(self, restore_data: dict) -> None:
        self.delete_old_backups_days.set(restore_data.get(SaveSettings.delete_old_backups_days, 1))

    def append_output(self, message):
        self.main_config.append_output(message)
