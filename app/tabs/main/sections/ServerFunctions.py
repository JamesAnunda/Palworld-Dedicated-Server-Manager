import tkinter as tk
from tkinter import ttk

from app.tabs.main import MainConfig
from app.utilities import Commands, TkViewElements


class ServerFunctions(TkViewElements.TkLabelFrame):
    commands_instance: Commands = None

    def __init__(self, main_config: 'MainConfig.MainConfig', label_text: str = "Server Functions", column: int = 0, row: int = 2, sticky: tk.constants = tk.NSEW):
        super().__init__(main_config, label_text, column, row, sticky)
        self.main_config: MainConfig = main_config

        row = 0
        self.functions_combobox = ttk.Combobox(self, justify="center", state="readonly", values=["Start Server", "Graceful Shutdown", "Force Shutdown", "Update Server", "Validate Server Files", "Backup Server"])
        self.functions_combobox.grid(column=0, row=row, padx=10, pady=10)
        self.functions_combobox.set("-SELECT-")
        ttk.Button(self, text="Execute", command=self.execute_function).grid(column=1, row=row)

    def set_commands_instance(self, commands_instance: 'Commands.Commands'):
        pass

    def execute_function(self) -> None:  #todo maybe this return type?
        pass

    def append_output(self, message) -> None:
        self.main_config.append_output(message)
