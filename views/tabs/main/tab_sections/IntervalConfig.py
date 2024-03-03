import tkinter as tk
from tkinter import ttk

from tktimepicker import constants, SpinTimePickerModern

from utilities.StateInterfaces import IRestorable, ISavable
from utilities.ValidationMethods import hours_validate
from views.tabs import TkViewElements
from views.tabs.main import MainConfig


class IntervalConfig(TkViewElements.TkLabelFrame, ISavable, IRestorable):
    def __init__(self, owning_tab: 'MainConfig.MainConfig', label_text: str = "Interval Configs", column: int = 0, row: int = 0, sticky: tk.constants = tk.NSEW):
        super().__init__(owning_tab, label_text, column, row, sticky)
        self.time_window: tk.Toplevel = None
        self.parent = owning_tab
        hours_validation = (self.register(hours_validate), '%P', '%d')

        # restart every X hours input
        self.interval_restart_bool = tk.BooleanVar(value=False)
        self.interval_restart_hours = tk.IntVar()
        ttk.Checkbutton(self, variable=self.interval_restart_bool, command=None).grid(row=0, column=0, sticky=tk.W)  #enable_server_restart
        ttk.Label(self, text="Server Restart Interval (hours):").grid(column=1, row=0, sticky=tk.W)
        ttk.Entry(self, textvariable=self.interval_restart_hours, width=3, validate="key", validatecommand=hours_validation).grid(column=2, row=0, sticky=tk.W)

        # restart at a given time input
        self.daily_restart_bool = tk.BooleanVar(value=False)
        self.daily_restart_time = tk.StringVar(value="12:00 AM")
        ttk.Checkbutton(self, variable=self.daily_restart_bool, command=None).grid(column=0, row=1, sticky=tk.W)  #enable_scheduled_restart
        ttk.Label(self, text="Daily Server Restart Time (12-hour Format):").grid(column=1, row=1, sticky=tk.W)
        ttk.Label(self, textvariable=self.daily_restart_time).grid(column=2, row=1, sticky=tk.W)
        self.time_picker_button = ttk.Button(self, text="Set", command=lambda: self.get_time(self.time_picker_button))
        self.time_picker_button.grid(column=3, row=1, sticky=tk.W)

        # how frequently to check if the server is running
        self.monitor_interval_bool = tk.BooleanVar(value=False)
        self.monitor_interval_int = tk.IntVar()
        ttk.Checkbutton(self, variable=self.monitor_interval_bool, command=None).grid(column=0, row=2, sticky=tk.W)
        ttk.Label(self, text="Monitor Interval (minutes):").grid(column=1, row=2, sticky=tk.W)
        ttk.Entry(self, textvariable=self.monitor_interval_bool, width=3).grid(column=2, row=2, sticky=tk.W)

        # backup every X hours
        self.backup_server_interval_bool = tk.BooleanVar(value=False)
        self.backup_server_interval_int = tk.IntVar()
        ttk.Checkbutton(self, variable=self.backup_server_interval_bool, command=None).grid(column=0, row=3, sticky=tk.W)
        ttk.Label(self, text="Backup Server Interval (hours):").grid(column=1, row=3, sticky=tk.W)
        ttk.Entry(self, textvariable=self.backup_server_interval_int, width=3).grid(column=2, row=3, sticky=tk.W)

    def save(self) -> dict:
        return {
                "interval_restart_hours": self.interval_restart_hours.get(),
                "daily_restart_time":     self.daily_restart_time.get(),
                # "monitor_interval_minutes":self.get_monitor_interval_minutes(),
                # "backup_interval_hours":   self.get_backup_interval_hours()
        }

    def restore(self, restore_data: dict) -> None:
        self.interval_restart_hours = restore_data.get("interval_restart_hours", 0)
        self.daily_restart_time = restore_data.get("daily_restart_time", "")
        self.monitor_interval_int = restore_data.get("monitor_interval_minutes", 0)
        self.backup_server_interval_int = restore_data.get("backup_interval_hours", 0)

    def get_time(self, button: tk.Button):
        (hours, minutes, period) = self.daily_restart_time.get().replace(":", " ").split(' ')

        if self.time_window is not None:
            return self.time_window.focus_set()
        self.time_window = tk.Toplevel(button)
        time_picker = SpinTimePickerModern(self.time_window, period=period, min_interval=15)
        time_picker.set12Hrs(hours)
        time_picker.setMins(minutes)
        time_picker.addAll(constants.HOURS12)
        time_picker.configureAll(height=1, font=("Times", 12), clickedbg="#2e2d2d", clickedcolor="#d73333")
        time_picker.pack(expand=True, fill="both")
        ok_btn = tk.Button(self.time_window, text="Set", command=lambda: self.update_daily_restart_time(time_picker.time()))
        cancel_btn = tk.Button(self.time_window, text="Cancel", command=self.destroy_time_window)
        ok_btn.pack(side=tk.LEFT)
        cancel_btn.pack(side=tk.RIGHT)
        self.time_window.geometry("+%d+%d"%(button.winfo_x(), button.winfo_y()))
        self.time_window.protocol("WM_DELETE_WINDOW", self.destroy_time_window)

    def update_daily_restart_time(self, time):
        self.daily_restart_time.set('{:02d}:{:02d} {}'.format(*time))
        self.destroy_time_window()

    def destroy_time_window(self):
        self.time_window.destroy()
        self.time_window.update()
        self.time_window = None
