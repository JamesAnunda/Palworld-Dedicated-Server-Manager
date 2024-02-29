import tkinter as tk

from views.tabs import TkViewElements
from views.tabs.main.MainView import MainView


class IntervalConfigView(TkViewElements.TkLabelFrame):
    def __init__(self, owning_tab: MainView, label_text: str = "Interval Configs", column: int = 0, row: int = 0, sticky: tk.constants = tk.NSEW):
        super().__init__(owning_tab, label_text, column, row, sticky)
