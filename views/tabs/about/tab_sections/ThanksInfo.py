import tkinter as tk
from tkinter import ttk

from utilities import TkViewElements
from views.tabs.about import About


class ThanksInfo(TkViewElements.TkLabelFrame):
    def __init__(self, about: 'About.About', label_text: str = "Special Thanks to the following Supporters", column: int = 0, row: int = 2, sticky: tk.constants = tk.EW):
        super().__init__(about, label_text, column, row, sticky)
        self.about: About = about
        self.supporters: list[str] = ["daisame.bsky.social", "CBesty"]  # todo: read supporters in from text file in root dir (next to version.txt)
        self.supporters: list[list[str]] = list(self.organize_supporters(5))

        for (table_row, row_supporters) in zip(range(0, len(self.supporters)), self.supporters):
            for (table_column, supporter) in zip(range(0, len(row_supporters)), row_supporters):
                ttk.Label(self, text=supporter).grid(column=table_column, row=table_row, padx=10, pady=10)

    def organize_supporters(self, n: int) -> list[list[str]]:
        """
        Cut Supporters list into n-sized chunks
        """
        for i in range(0, len(self.supporters), n):
            yield self.supporters[i:i+n]
