import tkinter as tk
from tkinter import ttk


class TkTab(ttk.Frame):
    """
    A class that represents a tab, extends a tkinter.ttk.Frame
    """

    def __init__(self, tab_control: ttk.Notebook, tab_name: str, index: int, weight: int = 1):
        super().__init__(tab_control)
        tab_control.add(self, text=tab_name)
        self.columnconfigure(index, weight=weight)

class TkLabelFrame(ttk.LabelFrame):
    """
    A class that represents a part of a TkTab, extends a tkinter.ttk.LabelFrame
    """

    def __init__(self, owning_tab: TkTab, label_text: str, column: int, row: int, sticky: tk.constants, padx: int = 10, pady: int = 10):
        super().__init__(owning_tab, text=label_text)
        self.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
        pass
