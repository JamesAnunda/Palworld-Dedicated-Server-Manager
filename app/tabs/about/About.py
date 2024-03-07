from app import Application
from app.tabs.about.sections import ApplicationInfo, SupportInfo, ThanksInfo
from app.utilities import TkViewElements


class About(TkViewElements.TkTab):
    """
    Tab Element, has subordinate elements

    Creates and tracks the following components: Interval Configs, Optional Configs, Server Info, and Server Functions
    """
    application_info: ApplicationInfo = None
    support_info: SupportInfo = None
    supporter_thanks: ThanksInfo = None

    def __init__(self, application: 'Application.Application', tab_name: str = "About"):
        super().__init__(application.get_tab_control(), tab_name)
        self.application: Application = application
        self.create_subcomponents()

    def create_subcomponents(self) -> None:
        self.application_info: ApplicationInfo = ApplicationInfo.ApplicationInfo(self)
        self.support_info: SupportInfo = SupportInfo.SupportInfo(self)
        self.supporter_thanks: ThanksInfo = ThanksInfo.ThanksInfo(self)

    def append_output(self, message) -> None:
        self.application.append_output(message)
