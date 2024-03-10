import os
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename

from app.handlers import SettingsHandler
from app.tabs.main import MainConfig
from app.utilities import TkViewElements
from app.utilities.StateInterfaces import IRestorable, ISavable


class SaveConfigs(TkViewElements.TkLabelFrame, ISavable, IRestorable):
    def __init__(self, main_config: 'MainConfig.MainConfig', settings_handler: 'SettingsHandler.SettingsHandler', label_text: str = "Save Configs", column: int = 1, row: int = 1, sticky: tk.constants = tk.NSEW):
        super().__init__(main_config, label_text, column, row, sticky)
        self.main_config: MainConfig = main_config
        self.settings_handler: SettingsHandler = settings_handler

        self.settings_location = tk.StringVar()
        self.formatted_path = tk.StringVar()
        row = 0
        ttk.Label(self, text="Save File Location: ").grid(column=0, row=row, sticky=tk.W)
        ttk.Label(self, textvariable=self.formatted_path, width=50).grid(column=1, row=row, sticky=tk.W)

        row += 1
        ttk.Button(self, text="Set Location", command=self.set_file_location).grid(column=1, row=row, sticky=tk.W)
        ttk.Button(self, text="Save Settings", command=self.save_all).grid(column=0, row=row, sticky=tk.W)

    def save(self) -> None:
        self.settings_handler.settings_location.set(self.settings_location.get())

    def save_all(self):
        self.main_config.append_output("Settings Saved!")
        self.main_config.application.save(one_off=True)

    def restore(self) -> None:
        self.settings_location.set(self.settings_handler.settings_location.get())
        self.format_path()

    def format_path(self):
        self.formatted_path.set(self.settings_location.get())
        max_len = 50
        if len(self.formatted_path.get()) > max_len:
            temp = [""]
            chunks = [chunk + '/' for chunk in self.formatted_path.get().split(os.path.sep)]
            chunks[-1] = chunks[-1].replace('/', "")
            for chunk in chunks:
                if len(chunk) + len(temp[-1]) > max_len:
                    temp.append("")
                temp[-1] = chunk if temp[-1] is None else temp[-1] + chunk
            self.formatted_path.set('\n'.join(temp))

    def set_file_location(self):
        temp = tk.filedialog.askopenfilename()
        if temp is None or temp == "":
            return
        self.settings_location.set(temp)
        self.format_path()
