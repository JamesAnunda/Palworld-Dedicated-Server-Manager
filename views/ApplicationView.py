import tkinter as tk
from tkinter import ttk

from controllers.ApplicationController import ApplicationController


class ApplicationView(tk.Tk):
    def __init__(self, controller: ApplicationController):
        super().__init__()
        self.controller: ApplicationController = controller
        self.tab_control: ttk.Notebook = ttk.Notebook(self)


        # self.main_view=MainView(tab_control=self.tab_control)
        # self.title("Palworld Dedicated Server Manager")
        # self.tab_control.pack(expand=1, fill="both")
        # # self.protocol("WM_DELETE_WINDOW", on_exit)
        # self.mainloop()
