from app import Application
from app.tabs.alerts_config.sections import DiscordConfig, EmailConfig
from app.utilities import TkViewElements
from app.utilities.StateInterfaces import IRestorable, ISavable


class AlertsConfig(TkViewElements.TkTab, ISavable, IRestorable):
    discord_config: DiscordConfig = None
    email_config: EmailConfig = None

    def __init__(self, application: 'Application.Application', tab_name: str = "Alerts Config"):
        super().__init__(application.get_tab_control(), tab_name, index=[0, 1])
        self.application: Application = application
        self.create_subcomponents()

    def create_subcomponents(self) -> None:
        self.email_config = EmailConfig.EmailConfig(self, self.application.settings_handler)
        self.discord_config = DiscordConfig.DiscordConfig(self, self.application.settings_handler)

    def save(self) -> None:
        self.discord_config.save()
        self.email_config.save()

    def restore(self) -> None:
        self.discord_config.restore()
        self.email_config.restore()
