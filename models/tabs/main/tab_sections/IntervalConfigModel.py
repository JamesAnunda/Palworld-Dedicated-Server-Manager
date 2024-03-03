from typing import Self

from utilities.StateInterfaces import IRestorable, ISavable


class IntervalConfigModel(ISavable, IRestorable):
    """
    Data storage/truth source class for IntervalConfigController
    Does not manage View, use the Controller for that
    """

    def __init__(self):
        self.do_interval_restart: bool = False
        self.interval_restart_hours: int = 0

        self.do_daily_restart: bool = False
        """Value is string, 12-hr format"""
        self.daily_restart_time: str = ""
        """Value is either AM or PM"""
        self.daily_restart_ampm: str = ""

        self.do_monitor_interval: bool = False
        self.monitor_interval_minutes: int = 0

        self.do_backup_interval: bool = False
        self.backup_interval_hours: int = 0
        pass

    def toggle_do_interval_restart(self) -> Self:
        self.do_interval_restart = not self.do_interval_restart
        return self

    def set_interval_restart_hours(self, interval_restart_hours: int) -> Self:
        self.interval_restart_hours = interval_restart_hours
        return self

    def toggle_do_daily_restart(self) -> Self:
        self.do_daily_restart = not self.do_daily_restart
        return self

    def set_daily_restart_time(self, restart_time: str) -> Self:
        self.daily_restart_time = restart_time
        return self

    def set_daily_restart_ampm(self, ampm: str) -> Self:
        self.daily_restart_ampm = ampm.upper()
        return self

    def toggle_do_monitor_interval(self) -> Self:
        self.do_monitor_interval = not self.do_monitor_interval
        return self

    def set_monitor_interval_minutes(self, monitor_interval_minutes: int) -> Self:
        self.monitor_interval_minutes = monitor_interval_minutes
        return self

    def toggle_do_backup_interval(self) -> Self:
        self.do_backup_interval = not self.do_backup_interval
        return self

    def set_backup_interval_hours(self, backup_interval_hours: int) -> Self:
        self.backup_interval_hours = backup_interval_hours
        return self

    def get_do_interval_restart(self) -> bool:
        return self.do_interval_restart

    def get_interval_restart_hours(self) -> int:
        return self.interval_restart_hours

    def get_do_daily_restart(self) -> bool:
        return self.do_daily_restart

    def get_daily_restart_time(self) -> str:
        return self.daily_restart_time

    def get_daily_restart_ampm(self) -> str:
        return self.daily_restart_ampm

    def get_do_monitor_interval(self) -> bool:
        return self.do_monitor_interval

    def get_monitor_interval_minutes(self) -> int:
        return self.monitor_interval_minutes

    def get_do_backup_interval(self) -> bool:
        return self.do_backup_interval

    def get_backup_interval_hours(self) -> int:
        return self.backup_interval_hours

    def save(self) -> dict:
        return {
                "interval_restart_hours":  self.get_interval_restart_hours(),
                "daily_restart_time":      self.get_daily_restart_time(),
                "daily_restart_ampm":      self.get_daily_restart_ampm(),
                "monitor_interval_minutes":self.get_monitor_interval_minutes(),
                "backup_interval_hours":   self.get_backup_interval_hours()
        }

    def restore(self, restore_data: dict):
        self.set_interval_restart_hours(restore_data.get("interval_restart_hours", 0))
        self.set_daily_restart_time(restore_data.get("daily_restart_time", ""))
        self.set_daily_restart_ampm(restore_data.get("daily_restart_ampm", "AM"))
        self.set_monitor_interval_minutes(restore_data.get("monitor_interval_minutes", 0))
        self.set_backup_interval_hours(restore_data.get("backup_interval_hours", 0))
