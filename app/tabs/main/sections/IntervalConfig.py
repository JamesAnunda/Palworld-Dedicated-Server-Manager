import tkinter as tk
from tkinter import font
from tkinter import ttk

from tktimepicker import constants, SpinTimePickerModern

from app.handlers import SettingsHandler
from app.tabs.main import MainConfig
from app.utilities import TkViewElements
from app.utilities.StateInterfaces import IRestorable, ISavable
from app.utilities.ValidationMethods import hours_validate, minutes_validate


class IntervalConfig(TkViewElements.TkLabelFrame, ISavable, IRestorable):
    """
    Last level of UI elements, directly creates the visual items

    Specifically, handles all things processed on an interval (restarts, backups, "is running" monitoring)
    """

    time_window: tk.Toplevel | None = None

    def __init__(self, main_config: 'MainConfig.MainConfig', settings_handler: 'SettingsHandler.SettingsHandler', label_text: str = "Interval Configs", column: int = 0, row: int = 0, sticky: tk.constants = tk.NSEW):
        super().__init__(main_config, label_text, column, row, sticky)
        self.main_config: MainConfig = main_config
        self.settings_handler: SettingsHandler = settings_handler

        hours_validation = (self.register(hours_validate), '%P', '%d', 24)
        minutes_validation = (self.register(minutes_validate), '%P', '%d', 99)

        row = 0
        # restart every X hours input
        self.interval_restart_bool = tk.BooleanVar(value=False)
        self.interval_restart_hours = tk.StringVar()
        ttk.Checkbutton(self, variable=self.interval_restart_bool, command=None).grid(column=0, row=row, sticky=tk.W)  # todo enable_interval_server_restart
        ttk.Label(self, text="Server Restart Interval (hours):").grid(column=1, row=row, sticky=tk.W)
        ttk.Entry(self, textvariable=self.interval_restart_hours, width=3, validate="key", validatecommand=hours_validation).grid(column=2, row=row, sticky=tk.W)

        row += 1
        # restart at a given time input
        self.daily_restart_bool = tk.BooleanVar(value=False)
        self.daily_restart_time = tk.StringVar(value=self.settings_handler.daily_restart_time.get())
        ttk.Checkbutton(self, variable=self.daily_restart_bool, command=None).grid(column=0, row=row, sticky=tk.W)  # todo enable_scheduled_restart
        ttk.Label(self, text="Daily Server Restart Time (12-hour Format):").grid(column=1, row=row, sticky=tk.W)
        time_font = font.nametofont("TkDefaultFont").copy()
        time_font.configure(weight="bold")
        ttk.Label(self, textvariable=self.daily_restart_time, font=time_font).grid(column=2, row=row, sticky=tk.W)
        self.time_picker_button = ttk.Button(self, text="Set", command=lambda: self.get_time(self.time_picker_button))
        self.time_picker_button.grid(column=3, row=row, sticky=tk.W)

        row += 1
        # how frequently to check if the server is running
        self.monitor_interval_bool = tk.BooleanVar(value=False)
        self.monitor_interval_minutes = tk.StringVar()
        ttk.Checkbutton(self, variable=self.monitor_interval_bool, command=None).grid(column=0, row=row, sticky=tk.W)  # todo enable_monitor
        ttk.Label(self, text="Monitor Interval (minutes):").grid(column=1, row=row, sticky=tk.W)
        ttk.Entry(self, textvariable=self.monitor_interval_minutes, width=3, validate="key", validatecommand=minutes_validation).grid(column=2, row=row, sticky=tk.W)

        row += 1
        # backup every X hours
        self.backup_interval_bool = tk.BooleanVar(value=False)
        self.backup_interval_hours = tk.StringVar()
        ttk.Checkbutton(self, variable=self.backup_interval_bool, command=None).grid(column=0, row=row, sticky=tk.W)  # todo enable_backup_interval
        ttk.Label(self, text="Backup Server Interval (hours):").grid(column=1, row=row, sticky=tk.W)
        ttk.Entry(self, textvariable=self.backup_interval_hours, width=3, validate="key", validatecommand=hours_validation).grid(column=2, row=row, sticky=tk.W)

    def save(self) -> None:
        self.settings_handler.interval_restart_hours.set(self.interval_restart_hours.get())
        self.settings_handler.daily_restart_time.set(self.daily_restart_time.get())
        self.settings_handler.monitor_interval_minutes.set(self.monitor_interval_minutes.get())
        self.settings_handler.backup_interval_hours.set(self.backup_interval_hours.get())

    def restore(self) -> None:
        self.interval_restart_hours.set(self.settings_handler.interval_restart_hours.get())
        self.daily_restart_time.set(self.settings_handler.daily_restart_time.get())
        self.monitor_interval_minutes.set(self.settings_handler.monitor_interval_minutes.get())
        self.backup_interval_hours.set(self.settings_handler.backup_interval_hours.get())

    def append_output(self, message) -> None:
        self.main_config.append_output(message)

    def get_time(self, button: tk.Button) -> None:
        (hours, minutes, period) = self.daily_restart_time.get().replace(":", " ").split(' ')

        self.time_window: tk.Toplevel = tk.Toplevel(button) if self.time_window is None else self.time_window.focus_set()
        self.time_window.title("")
        self.time_window.protocol("WM_DELETE_WINDOW", self.destroy_time_window)
        x = self.main_config.application.winfo_x() + button.winfo_x() + 100
        y = self.main_config.application.winfo_y() + button.winfo_y() + 25
        self.time_window.geometry("%dx%d+%d+%d" % (175, 75, x, y))

        time_picker = SpinTimePickerModern(self.time_window, period=period, min_interval=15)
        time_picker.set12Hrs(hours)
        time_picker.setMins(minutes)
        time_picker.addAll(constants.HOURS12)
        time_picker.configureAll(font=("Times", 12), clickedbg="#2e2d2d", clickedcolor="#d73333")
        time_picker.pack(expand=True, fill="both")
        ok_btn = tk.Button(self.time_window, text="Set", command=lambda: self.update_daily_restart_time(time_picker.time()))
        cancel_btn = tk.Button(self.time_window, text="Cancel", command=self.destroy_time_window)
        ok_btn.pack(side=tk.LEFT)
        cancel_btn.pack(side=tk.RIGHT)

    def update_daily_restart_time(self, time) -> None:
        self.daily_restart_time.set('{:02d}:{:02d} {}'.format(*time))
        self.destroy_time_window()

    def destroy_time_window(self) -> None:
        self.time_window.destroy()
        self.time_window.update()
        self.time_window = None

    def interval_restart_enabled(self):
        return self.interval_restart_bool.get()

    def daily_restart_enabled(self):
        return self.daily_restart_bool.get()

    def monitor_interval_enabled(self):
        return self.monitor_interval_bool.get()

    def backup_interval_enabled(self):
        return self.backup_interval_bool.get()
