import tkinter as tk

from utilities.StateInterfaces import IRestorable, ISavable
from views.tabs import TkViewElements
from views.tabs.main import MainConfig


class OptionalConfig(TkViewElements.TkLabelFrame, ISavable, IRestorable):
    def __init__(self, owning_tab: 'MainConfig.MainConfig', label_text: str = "Optional Configs", column: int = 0, row: int = 1, sticky: tk.constants = tk.NSEW):
        super().__init__(owning_tab, label_text, column, row, sticky)

    def save(self) -> dict:
        pass

    def restore(self, restore_data: dict) -> None:
        pass
