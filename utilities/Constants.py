class SaveSettings:
    interval_restart_hours = "interval_restart_hours"
    interval_restart_hours_default = 0

    daily_restart_time = "daily_restart_time"
    daily_restart_time_default = "12:00 AM"

    monitor_interval_minutes = "monitor_interval_minutes"
    monitor_interval_minutes_default = 0

    backup_interval_hours = "backup_interval_hours"
    backup_interval_hours_default = 0

    delete_old_backups_days = "delete_old_backups_days"
    delete_old_backups_days_default = 1

    palworld_directory = "palworld_directory"
    palworld_directory_default = "No Directory Selected"

    arrcon_directory = "arrcon_directory"
    arrcon_directory_default = "No Directory Selected"

    steamcmd_directory = "steamcmd_directory"
    steamcmd_directory_default = "No Directory Selected"

    backup_directory = "backup_directory"
    backup_directory_default = ""

    server_start_args = "server_start_args"
    server_start_args_default = "-useperfthreads -NoAsyncLoadingThread -UseMultithreadForDS -EpicApp=PalServer"
