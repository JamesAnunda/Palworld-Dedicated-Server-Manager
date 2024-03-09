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

        self.settings_file = tk.StringVar()
        self.settings_dir = tk.StringVar()
        self.full_path = tk.StringVar()
        row = 0
        ttk.Label(self, text="Save File Location: ").grid(column=0, row=row, sticky=tk.W)
        ttk.Label(self, textvariable=self.full_path, width=50).grid(column=1, row=row, sticky=tk.W)

        row += 1
        ttk.Button(self, text="Set Location", command=self.set_file_location).grid(column=0, row=row, columnspan=2, sticky=tk.S)

    def save(self) -> None:
        self.settings_handler.settings_file.set(self.settings_file.get())
        self.settings_handler.settings_directory.set(self.settings_dir.get())

    def restore(self) -> None:
        self.settings_file.set(self.settings_handler.settings_file.get())
        self.settings_dir.set(self.settings_handler.settings_directory.get())
        self.process_full_path()

    def process_full_path(self):
        self.full_path.set(os.path.join(self.settings_dir.get(), self.settings_file.get()))
        max_len = 50
        if len(self.full_path.get()) > max_len:
            temp = [""]
            chunks = [chunk + '/' for chunk in self.full_path.get().split(os.path.sep)]
            chunks[-1] = chunks[-1].replace('/', "")
            for chunk in chunks:
                if len(chunk) + len(temp[-1]) > max_len:
                    temp.append("")
                temp[-1] = chunk if temp[-1] is None else temp[-1] + chunk
            self.full_path.set('\n'.join(temp))

    def set_file_location(self):
        temp = tk.filedialog.askopenfilename()
        if temp is None or temp == "":
            return
        temp = os.path.split(temp)
        self.settings_dir.set(temp[0])
        self.settings_file.set(temp[1])
        self.process_full_path()
