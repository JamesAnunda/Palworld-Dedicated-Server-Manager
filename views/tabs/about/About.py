from utilities import TkViewElements
from views import Application
from views.tabs.about.tab_sections import ApplicationInfo, SupportInfo, ThanksInfo


class About(TkViewElements.TkTab):
    """
    Tab Element, has subordinate elements

    Creates and tracks the following components: Interval Configs, Optional Configs, Server Info, and Server Functions
    """
    application_info = None
    support_info = None
    supporter_thanks = None

    def __init__(self, application: 'Application.Application', tab_name: str = "About"):
        super().__init__(application.get_tab_control(), tab_name)
        self.application = application
        self.create_subcomponents()

    def create_subcomponents(self):
        self.application_info = ApplicationInfo.ApplicationInfo(self)
        self.support_info = SupportInfo.SupportInfo(self)
        self.supporter_thanks = ThanksInfo.ThanksInfo(self)

    def append_output(self, message):
        self.application.append_output(message)
