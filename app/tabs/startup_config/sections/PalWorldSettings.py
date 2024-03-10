import os
import platform
import re
import subprocess
import threading
import tkinter as tk
from tkinter import messagebox, ttk

from app.handlers import SettingsHandler
from app.tabs.startup_config import StartupConfigs
from app.utilities import TkViewElements
from app.utilities.StateInterfaces import IRestorable


class PalWorldSettings(TkViewElements.TkLabelFrame, IRestorable):
    def __init__(self, startup_configs: 'StartupConfigs.StartupConfigs', settings_handler: 'SettingsHandler.SettingsHandler', label_text: str = "PalWorldSettings.ini", column: int = 0, row: int = 0, sticky: tk.constants = tk.constants.N):
        super().__init__(startup_configs, label_text, column, row, sticky)
        self.startup_configs: StartupConfigs = startup_configs
        self.settings_handler: SettingsHandler = settings_handler

        self.server_name = tk.StringVar(value="-")
        self.server_desc = tk.StringVar(value="-")
        self.server_pass = tk.StringVar(value="-")
        self.max_players = tk.StringVar(value="-")
        self.server_port = tk.StringVar(value="-")
        self.rcon_port = tk.StringVar(value="-")
        self.rcon_enabled = tk.StringVar(value="-")
        self.rcon_pass = tk.StringVar(value="-")

        self.create_setting_view("Server Name:", self.server_name, 0, 0)
        self.create_setting_view("Server Description:", self.server_desc, 0, 2)
        self.server_pass_label = self.create_setting_view("Server Password:", None, 0, 4)
        self.create_setting_view("Max Players:", self.max_players, 1, 0)
        self.create_setting_view("Server Port:", self.server_port, 1, 2)
        self.create_setting_view("RCON Port:", self.rcon_port, 2, 0)
        self.create_setting_view("RCON Enabled:", self.rcon_enabled, 2, 2)
        self.rcon_pass_label = self.create_setting_view("RCON Password:", None, 2, 4)

        ttk.Button(self, text="Edit PalWorldSettings.ini", command=self.open_palworld_settings).grid(column=0, row=6, columnspan=3, padx=10, pady=10)

    def save(self) -> None:
        self.settings_handler.rcon_port.set(self.rcon_port.get())
        self.settings_handler.rcon_pass.set(self.rcon_pass.get())

    def restore(self) -> None:
        self.update_settings()

    def append_output(self, message) -> None:
        self.startup_configs.append_output(message)

    def create_setting_view(self, label_text, var, column, row) -> ttk.Label:
        ttk.Label(self, text=label_text).grid(column=column, row=row, padx=10, sticky=tk.W)
        var_label = ttk.Label(self, textvariable=var)
        var_label.grid(column=column, row=row + 1, padx=10, sticky=tk.W)
        return var_label

    def reset_server_info(self):
        self.rcon_port.set("-")
        self.rcon_enabled.set("-")
        self.rcon_pass_label.config(text="-")
        self.max_players.set("-")
        self.server_name.set("-")
        self.server_desc.set("-")
        self.server_pass_label.config(text="-")
        self.server_port.set("-")

    def update_settings(self) -> None:
        directory = self.startup_configs.application.settings_handler.palworld_location.get()
        if directory == self.startup_configs.application.settings_handler.palworld_location.get_default():
            self.reset_server_info()
            return self.invalid_directory()
        file_path = os.path.join(directory, 'Pal', 'Saved', 'Config', 'WindowsServer', 'PalWorldSettings.ini')
        if not os.path.exists(file_path) or not os.path.isfile(file_path):
            self.reset_server_info()
            return self.invalid_directory()

        with open(file_path, 'r') as file:
            file_content = file.read()
            max_players_match = re.search(r'ServerPlayerMaxNum=(\d+),', file_content)
            server_name_match = re.search(r'ServerName="([^"]+)",', file_content)
            server_description_match = re.search(r'ServerDescription="([^"]+)",', file_content)
            server_password_match = re.search(r'ServerPassword="([^"]*)",', file_content)
            server_port_match = re.search(r'PublicPort=(\d+),', file_content)
            rcon_port_match = re.search(r'RCONPort=(\d+),', file_content)
            rcon_enable_match = re.search(r'RCONEnabled=(\w+),', file_content)
            rcon_password_match = re.search(r'AdminPassword="([^"]*)",', file_content)

            self.rcon_port.set(rcon_port_match.group(1) if rcon_port_match else "-")
            self.server_port.set(server_port_match.group(1) if server_port_match else "-")
            self.max_players.set(max_players_match.group(1) if max_players_match else "-")
            self.server_name.set(server_name_match.group(1) if server_name_match else "-")
            self.rcon_enabled.set(rcon_enable_match.group(1) if rcon_enable_match else "-")
            self.server_desc.set(server_description_match.group(1) if server_description_match else "-")

            if rcon_password_match:
                rcon_pass = rcon_password_match.group(1)
                self.rcon_pass.set(rcon_pass)
                self.rcon_pass_label.config(text="No Password Set" if rcon_pass == "" else "****")
            if server_password_match:
                server_pass = server_password_match.group(1)
                self.server_pass.set(server_pass)
                self.server_pass_label.config(text="No Password Set" if server_pass == "" else "****")

    def open_palworld_settings(self) -> None:
        directory = self.startup_configs.application.settings_handler.palworld_location.get()
        if directory == self.startup_configs.application.settings_handler.palworld_location.get_default():
            return self.invalid_directory()
        ini_file_path = os.path.join(directory, 'Pal', 'Saved', 'Config', 'WindowsServer', 'PalWorldSettings.ini')
        if not os.path.exists(ini_file_path) or not os.path.isfile(ini_file_path):
            return self.invalid_directory()

        try:  # todo in the making: initial attempt at multi-platform support
            if platform.system() == 'Darwin':  # macOS
                args = [['open', '-a', 'TextEdit', ini_file_path], False]  # -a = use this application
            elif platform.system() == 'Windows':
                args = [['start', '/WAIT', ini_file_path], True]
            else:  # linux
                args = [['xdg-open', ini_file_path], False]
            popen_and_call(self.update_settings, args[0], args[1])  # enables async editing with callback
        except Exception as e:
            self.append_output("Error opening file: " + str(e))

    def invalid_directory(self):
        self.append_output("You need to select a valid directory first.")
        messagebox.showinfo("Invalid Directory", "You need to select a valid directory first")

def popen_and_call(on_exit, popen_args, shell):
    """
    Runs the given args in a subprocess.Popen, and then calls the function on_exit when the subprocess completes.
    on_exit is a callable object, and popen_args is a list/tuple of args that would give to subprocess.Popen.
    """

    def run_in_thread(_callback, _args, _shell):
        subprocess.Popen(_args, shell=_shell).wait()
        return _callback()

    thread = threading.Thread(target=run_in_thread, args=(on_exit, popen_args, shell))
    thread.start()
    return thread  # returns immediately after the thread starts
