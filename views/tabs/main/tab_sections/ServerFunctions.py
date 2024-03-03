import tkinter as tk
from tkinter import ttk

from views.tabs import TkViewElements
from views.tabs.main import MainConfig


class ServerFunctions(TkViewElements.TkLabelFrame):

    def __init__(self, main_config: 'MainConfig.MainConfig', label_text: str = "Server Functions", column: int = 0, row: int = 2, sticky: tk.constants = tk.NSEW):
        super().__init__(main_config, label_text, column, row, sticky)
        self.main_config = main_config

        self.functions_combobox = ttk.Combobox(self, justify="center", state="readonly", values=["Start Server", "Graceful Shutdown", "Force Shutdown", "Update Server", "Validate Server Files", "Backup Server"])
        self.functions_combobox.grid(column=0, row=0, padx=10, pady=10)
        self.functions_combobox.set("-SELECT-")
        ttk.Button(self, text="Execute", command=self.execute_function).grid(column=1, row=0)

    def execute_function(self):
        pass
