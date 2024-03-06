from utilities import TkViewElements
from utilities.StateInterfaces import IRestorable, ISavable
from views import Application
from views.tabs.alerts_config.tab_sections import DiscordConfig, EmailConfig


class AlertsConfig(TkViewElements.TkTab, ISavable, IRestorable):
    discord_config: DiscordConfig = None
    email_config: EmailConfig = None

    def __init__(self, application: 'Application.Application', tab_name: str = "Alerts Config"):
        super().__init__(application.get_tab_control(), tab_name, index=[0, 1])
        self.application: Application = application
        self.create_subcomponents()

    def create_subcomponents(self) -> None:
        self.email_config = EmailConfig.EmailConfig(self)
        self.discord_config = DiscordConfig.DiscordConfig(self)

    def save(self) -> dict:
        return self.discord_config.save() | self.email_config.save()

    def restore(self, restore_data: dict) -> None:
        self.discord_config.restore(restore_data)
        self.email_config.restore(restore_data)
