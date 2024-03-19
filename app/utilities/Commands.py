import datetime
import os
import subprocess
import zipfile
from tkinter import messagebox

from app import Application


class Commands:
    UPDATE_SUCCESS = "UP_Success"
    UPDATE_FAIL = "UP_Fail"
    EXECUTE_SUCCESS = "EX_Success"
    EXECUTE_FAIL = "EX_Fail"

    def __init__(self, application: 'Application.Application'):
        self.application: Application = application

    def execute_command(self, command: str, command_name: str):
        try:
            subprocess.Popen(command)
            return Commands.EXECUTE_SUCCESS
        except Exception as e:
            self.application.append_output(f"Could not execute '{command_name}': " + str(e))
            return Commands.EXECUTE_FAIL

    def get_arrcon_prefix(self) -> str:
        return f'{self.application.settings_handler.arrcon_location.get()}/arrcon.exe -H 127.0.0.1 -P {self.application.settings_handler.rcon_port.get()} -p {self.application.settings_handler.rcon_pass.get()} '

    def get_steam_palworld_loc(self):
        return [self.application.settings_handler.steamcmd_location.get(), self.application.settings_handler.palworld_location.get()]

    def save_server(self):
        cmd = self.get_arrcon_prefix() + '"save"'
        self.execute_command(cmd, "Save Server")

    def info_server(self):
        cmd = self.get_arrcon_prefix() + '"info"'
        self.execute_command(cmd, "Info Server")

    def update_server(self):
        steamcmd_loc, palworld_loc = self.get_steam_palworld_loc()
        cmd = f'call {steamcmd_loc}/steamcmd.exe +force_install_dir {palworld_loc} +login anonymous +app_update 2394010 +quit'
        self.execute_command(cmd, "Update Server")

    def validate_server(self):
        steamcmd_loc, palworld_loc = self.get_steam_palworld_loc()
        cmd = f'call {steamcmd_loc}/steamcmd.exe +force_install_dir {palworld_loc} +login anonymous +app_update 2394010 validate +quit'
        self.execute_command(cmd, "Validate Server")

    def graceful_shutdown(self):
        cmd = self.get_arrcon_prefix() + '"shutdown 60 The_server_will_be_restarting_in_60_seconds"'
        self.execute_command(cmd, "Graceful Shutdown Server")

    def force_shutdown(self):
        cmd = self.get_arrcon_prefix() + '"doexit"'
        self.execute_command(cmd, "Force Shutdown Server")

    def start_server(self):
        steamcmd_loc, palworld_loc = self.get_steam_palworld_loc()
        cmd = f'{palworld_loc}/PalServer.exe {self.application.settings_handler.server_start_args.get()}'
        self.execute_command(cmd, "Start Server")

    def broadcast_message(self, time_seconds):
        cmd = self.get_arrcon_prefix() + '"broadcast The_server_will_be_restarting_in_{}_seconds"'.format(time_seconds)
        self.execute_command(cmd, "Broadcast Server Restart Message")

    def backup_server(self):
        if self.application.settings_handler.palworld_location.is_default():
            self.application.append_output("You must select a valid Palworld Server Directory to use this function. Check your Server Config tab")
            messagebox.showinfo("Invalid Directory", "You must select a valid Palworld Server directory to use this function")
            return

        if self.application.settings_handler.backup_location.is_default():
            self.application.append_output("You must select a Backup Directory to use this function. Check your Server Config tab")
            messagebox.showinfo("Invalid Directory", "You must select a valid Backup directory to use this function")
            return

        palworld_directory = self.application.settings_handler.palworld_location.get()
        backup_dir = self.application.settings_handler.backup_location.get()
        source_dir = f"{palworld_directory}/Pal/Saved/SaveGames/0"

        os.makedirs(backup_dir, exist_ok=True)  # Create the backup directory if it doesn't exist
        current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file_path = os.path.join(backup_dir, f"palworld_backup_{current_datetime}.zip")

        files_to_backup = []
        for root, dirs, files in os.walk(source_dir):
            files_to_backup.extend(os.path.join(root, file) for file in files)

        if files_to_backup:
            with zipfile.ZipFile(backup_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_archive:
                for root, dirs, files in os.walk(source_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, source_dir)
                        zip_archive.write(file_path, arcname=arcname)

        # Print a message indicating the completion of the backup
        if os.path.exists(backup_file_path):
            self.application.append_output(f"Backup of {source_dir} completed at {backup_file_path}")
        else:
            self.application.append_output("Backup FAILED!")

        if self.application.settings_handler.delete_old_backups_enabled.get():
            current_time = datetime.datetime.now()
            days_entry = int(self.application.settings_handler.delete_old_backups_days.get())
            self.application.append_output(str(days_entry))

            days_ago = current_time - datetime.timedelta(days = days_entry)
            backup_dir = self.application.settings_handler.backup_location.get()

            for filename in os.listdir(backup_dir):
                if filename.startswith("palworld_backup_"):
                    filepath = os.path.join(backup_dir, filename)

                    modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))

                    if modification_time < days_ago:
                        os.remove(filepath)
                        self.application.append_output(f"Old backup deleted: {filepath}")
