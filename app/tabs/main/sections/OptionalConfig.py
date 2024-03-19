import tkinter as tk
from tkinter import ttk

from app.handlers import SettingsHandler
from app.tabs.main import MainConfig
from app.utilities import TkViewElements
from app.utilities.StateInterfaces import IRestorable, ISavable
from app.utilities.ValidationMethods import numeric_validate


class OptionalConfig(TkViewElements.TkLabelFrame, ISavable, IRestorable):
    """
        Last level of UI elements, directly creates the visual items

        Specifically, handles all things regarding notifications and backup management
    """

    def __init__(self, main_config: 'MainConfig.MainConfig', settings_handler: 'SettingsHandler.SettingsHandler', label_text: str = "Optional Configs", column: int = 0, row: int = 1, sticky: tk.constants = tk.NSEW):
        super().__init__(main_config, label_text, column, row, sticky)
        self.main_config: MainConfig = main_config
        self.settings_handler: SettingsHandler = settings_handler

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
        self.delete_old_backups_bool = tk.BooleanVar(value=False)
        self.delete_old_backups_days = tk.StringVar()
        ttk.Checkbutton(self, variable=self.delete_old_backups_bool, command=None).grid(column=0, row=row, sticky=tk.W)  # todo enable_delete_backups
        ttk.Label(self, text="Delete Old Backups").grid(column=1, row=row, sticky=tk.W)
        ttk.Entry(self, textvariable=self.delete_old_backups_days, width=3, validate="key", validatecommand=(self.register(numeric_validate), '%P', '%d', 1, 365)).grid(column=2, row=row, sticky=tk.W)

    def save(self) -> None:
        self.settings_handler.send_email_on_crash_enabled.set(self.send_email_bool.get())
        self.settings_handler.send_discord_on_crash_enabled.set(self.send_discord_bool.get())
        self.settings_handler.check_update_on_start_enabled.set(self.check_update_startup_bool.get())
        self.settings_handler.backup_on_restart_enabled.set(self.backup_restart_bool.get())
        self.settings_handler.delete_old_backups_enabled.set(self.delete_old_backups_bool.get())
        self.settings_handler.delete_old_backups_days.set(self.delete_old_backups_days.get())

    def restore(self) -> None:
        self.delete_old_backups_days.set(self.settings_handler.delete_old_backups_days.get())

    def append_output(self, message) -> None:
        self.main_config.append_output(message)

    def email_notification_enabled(self):
        return self.send_email_bool.get()

    def discord_notification_enabled(self):
        return self.send_discord_bool.get()

    def startup_update_check_enabled(self):
        return self.check_update_startup_bool.get()

    def backup_during_restart_enabled(self):
        return self.backup_restart_bool.get()

    def delete_old_backups_enabled(self):
        return self.delete_old_backups_bool.get()
