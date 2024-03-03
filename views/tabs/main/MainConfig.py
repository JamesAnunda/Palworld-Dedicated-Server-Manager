from utilities.StateInterfaces import IRestorable, ISavable
from views import Application
from views.tabs import TkViewElements
from views.tabs.main.tab_sections import IntervalConfig, OptionalConfig


class MainConfig(TkViewElements.TkTab, ISavable, IRestorable):
    interval_config: IntervalConfig = None
    optional_config: OptionalConfig = None

    def __init__(self, parent: 'Application.Application', tab_name: str = "Main", index: int = 0):
        super().__init__(parent.get_tab_control(), tab_name, index)
        self.parent: Application = parent
        self.initial_setup()
        self.create_subcomponents()

    def save(self) -> dict:
        pass

    def restore(self, restore_data: dict) -> None:
        pass

    def initial_setup(self):
        # no op
        pass

    def create_subcomponents(self):
        self.interval_config = IntervalConfig.IntervalConfig(self)
        self.optional_config = OptionalConfig.OptionalConfig(self)
        pass
