import tkinter as tk
from datetime import datetime
from tkinter import ttk

from views import Application


class OutputConsole(tk.Frame):

    def __init__(self, application: 'Application.Application'):
        super().__init__(application)
        self.application = application
        self.pack(side="bottom", expand=True, fill=tk.BOTH)
        ttk.Label(self, text="Output Window").pack()

        scrollbar = ttk.Scrollbar(self, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        self.output_text = tk.Text(self, wrap=tk.WORD, height=10, width=85, yscrollcommand=scrollbar.set)
        self.output_text.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
        self.output_text.bind("<Key>", lambda e: "break")  # prevent typing into console
        scrollbar.config(command=self.output_text.yview)

    def append_output(self, message):
        message_time = datetime.now().astimezone()
        timezone = message_time.tzname().split(" ")
        tz_short = "] " if type(timezone) is not list else " "+timezone[0]+"/"+timezone[1][0]+timezone[2][0]+timezone[3][0]+"] "
        self.output_text.insert(tk.END, message_time.strftime("[%Y-%m-%d %H:%M:%S")+tz_short+message+"\n")
        self.output_text.yview(tk.END)  # Auto-scroll to the bottom
