from typing import Self


class IntervalConfigModel:
    """
    Data storage/truth source class for IntervalConfigController
    Does not manage View, does not handle validation
    """

    def __init__(self):
        self.do_interval_restart: bool=False
        self.interval_restart_hours: int=0
        self.do_daily_restart: bool=False
        """Value is string, 12-hr format"""
        self.daily_restart_hour_value: str=""
        """Value is either AM or PM"""
        self.daily_restart_ampm_value: str=""
        self.do_monitor_interval: bool=False
        self.monitor_interval_minutes: int=0
        self.do_backup_interval: bool=False
        self.backup_interval_hours: int=0
        pass

    def set_do_interval_restart(self, do_interval_restart: bool) -> Self:
        self.do_interval_restart=do_interval_restart
        return self

    def set_interval_restart_value(self, interval_restart_hours: int) -> Self:
        self.interval_restart_hours=interval_restart_hours
        return self

    def set_do_daily_restart(self, do_daily_restart: bool) -> Self:
        self.do_daily_restart=do_daily_restart
        return self

    def set_daily_restart_hour_value(self, restart_hour_value: int) -> Self:
        self.daily_restart_hour_value=restart_hour_value
        return self

    def set_daily_restart_ampm_value(self, ampm_value: str) -> Self:
        self.daily_restart_ampm_value=ampm_value.upper()
        return self

    def set_do_monitor_interval(self, do_monitor: bool) -> Self:
        self.do_monitor_interval=do_monitor
        return self

    def set_monitor_interval_value(self, monitor_interval_minutes: int) -> Self:
        self.do_monitor_interval=monitor_interval_minutes
        return self

    def set_do_backup_interval(self, do_interval_backup: bool) -> Self:
        self.do_backup_interval=do_interval_backup
        return self

    def set_backup_interval_value(self, backup_interval_hours: int) -> Self:
        self.backup_interval_hours=backup_interval_hours
        return self

    def get_do_interval_restart(self) -> bool:
        return self.do_interval_restart

    def get_interval_restart_hours(self) -> int:
        return self.interval_restart_hours

    def get_do_daily_restart(self) -> bool:
        return self.do_daily_restart

    def get_daily_restart_hours(self) -> str:
        return self.daily_restart_hour_value

    def get_daily_restart_ampm_value(self) -> str:
        return self.daily_restart_ampm_value

    def get_do_monitor_interval(self) -> bool:
        return self.do_monitor_interval

    def get_monitor_interval_minutes(self) -> int:
        return self.monitor_interval_minutes

    def get_do_backup_interval(self) -> bool:
        return self.do_backup_interval

    def get_do_backup_interval_hours(self) -> int:
        return self.backup_interval_hours
