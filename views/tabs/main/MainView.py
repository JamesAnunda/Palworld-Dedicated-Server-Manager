from controllers.tabs.main.MainController import MainController
from views.tabs import TkViewElements


class MainView(TkViewElements.TkTab):
    def __init__(self, controller: MainController, tab_name: str = "Main", index: int = 0):
        self.controller: MainController = controller
        super().__init__(self.controller.get_tab_control(), tab_name, index)
