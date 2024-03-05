import os
import tkinter as tk
from tkinter import ttk

from utilities import TkViewElements, Utilities
from views.tabs.about import About


class ApplicationInfo(TkViewElements.TkLabelFrame):

    def __init__(self, about: 'About.About', label_text: str = "Application Info", column: int = 0, row: int = 0, sticky: tk.constants = tk.N):
        super().__init__(about, label_text, column, row, sticky)
        self.about = about
        ttk.Label(self, text="Application Version: ").grid(column=0, row=0, padx=10, pady=10, sticky=tk.N)
        with open(os.path.join(self.about.application.root_path, 'version.txt'), 'r') as file:
            version = file.read().replace('\n', '').strip()
        ttk.Label(self, text=version).grid(column=1, row=0, padx=10, pady=10)
        ttk.Button(self, text="Check for Updates", command=self.check_for_updates).grid(column=0, row=1, columnspan=2, padx=10, pady=10)
        ttk.Button(self, text="Report a Bug", command=Utilities.report_bug).grid(column=0, row=2, columnspan=2, padx=10, pady=10)

    def append_output(self, message):
        self.about.append_output(message)

    def check_for_updates(self):
        # todo: get latest version from GitHub, check if the versions mismatch and popup if so w/ button link to GH
        pass
