from controllers.ApplicationController import ApplicationController


class ApplicationModel:
    def __init__(self, controller: ApplicationController):
        self.controller: ApplicationController = controller
        pass
