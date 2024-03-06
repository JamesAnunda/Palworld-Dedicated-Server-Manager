import tkinter as tk
from tkinter import ttk

from utilities import TkViewElements, Utilities
from views.tabs.about import About


class SupportInfo(TkViewElements.TkLabelFrame):
    def __init__(self, about: 'About.About', label_text: str = "Support Info", column: int = 0, row: int = 1, sticky: tk.constants = tk.EW):
        super().__init__(about, label_text, column, row, sticky)
        self.about: About = about

        row = 0
        ttk.Label(self, text="Have feedback or suggestions? Join my discord and let me know:").grid(column=0, row=row, sticky=tk.E)
        feedback_label_link = tk.Label(self, text="https://discord.gg/bPp9kfWe5t", foreground="blue", cursor="hand2")
        feedback_label_link.grid(column=1, row=row, sticky=tk.W)
        feedback_label_link.bind("<Button-1>", Utilities.open_discord)

        row += 1
        buy_me_beer_label = ttk.Label(self, justify="center", text="This application is completely free and no features will ever be behind a paywall. "
                                                                   "If you would like to support me I would greatly appreciate it. You can buy me a beer here:")
        buy_me_beer_label.grid(column=0, row=row, columnspan=2, sticky=tk.N)
        buy_me_beer_link = tk.Label(self, text="https://www.buymeacoffee.com/thewisestguy", foreground="blue", cursor="hand2")

        row += 1
        buy_me_beer_link.grid(column=0, row=row, columnspan=2)
        buy_me_beer_link.bind("<Button-1>", Utilities.open_BMAB)
