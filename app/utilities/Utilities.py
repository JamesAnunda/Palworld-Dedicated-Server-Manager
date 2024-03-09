import datetime
import smtplib
import time
import webbrowser
from email.message import EmailMessage
from enum import auto, Enum

import requests

from app import Application


class MessageLevel(Enum):
    ALL_CLEAR = (auto(), 0x00FF00)
    INFO = (auto(), 0x00FFFF)
    PLAYER_ACTION_REQUIRED = (auto(), 0xFF00FF)
    ADMIN_ACTION_REQUIRED = (auto(), 0xFFAA00)
    WARNING = (auto(), 0xF00600)
    ERROR = (auto(), 0x7F0000)

    def __init__(self, level, color: int):
        self.level = level
        self.color: hex = color

class MessageResponse:
    def __init__(self, success: bool, message_level: MessageLevel, response: str | None = None):
        self.success: bool = success
        self.message_level: MessageLevel = message_level
        self.response: str | None = response

class Utilities:
    application = None

    @classmethod
    def set_application(cls, application: 'Application.Application'):
        cls.application = application

    @staticmethod
    def open_discord(_ignored):
        webbrowser.open("https://discord.gg/bPp9kfWe5t")

    @staticmethod
    def open_bmab(_ignored):
        webbrowser.open("https://www.buymeacoffee.com/thewisestguy")

    @staticmethod
    def check_for_updates():
        webbrowser.open("https://github.com/Andrew1175/Palworld-Dedicated-Server-Manager/releases")

    @staticmethod
    def report_bug():
        webbrowser.open("https://github.com/Andrew1175/Palworld-Dedicated-Server-Manager/issues")

    @staticmethod
    def open_google_app_password(_ignored):
        webbrowser.open("https://support.google.com/accounts/answer/185833")

    @classmethod
    def send_discord_message(cls, message, message_level: MessageLevel) -> MessageResponse:
        if message is None or message == '':
            return MessageResponse(False, MessageLevel.ERROR, "Discord Webhook message is invalid")
        current_time = datetime.datetime.now().replace(microsecond=0)
        message = "Dispatched: <t:" + str(int(time.mktime(current_time.timetuple()))) + "> (your local time)\n" + message
        discord_webhook = cls.application.settings_handler.discord_webhook.get()
        if discord_webhook is None or discord_webhook == '':  # todo: further validation?
            return MessageResponse(False, MessageLevel.ADMIN_ACTION_REQUIRED, "Discord Webhook is invalid")

        try:
            payload = {
                    "embeds": [{
                            "title":       "PalServer Manager, Level: " + message_level.name.replace("_", " ").upper(),
                            "description": message,
                            "color":       message_level.color
                    }]
            }
            response = requests.post(discord_webhook, json=payload)
            response.raise_for_status()  #raise error exceptions, if present
            cls.application.append_output(f'Discord alert was sent: {message}')
            return MessageResponse(True, MessageLevel.ALL_CLEAR)
        except requests.exceptions.RequestException as e:
            cls.application.append_output(f"Error sending Discord alert: {e}\nIntended Discord message: {message}\nDiscord Webhook URL: {discord_webhook}")
            return MessageResponse(False, MessageLevel.ADMIN_ACTION_REQUIRED, f"Error sending Discord alert: {e}\nIntended Discord message: {message}\nDiscord Webhook URL: {discord_webhook}")

    @classmethod
    def send_test_discord_message(cls) -> MessageResponse:
        cls.send_discord_message("This is a test ALL_CLEAR message, **please ignore me**! There's nothing to worry about!", MessageLevel.ALL_CLEAR)
        cls.send_discord_message("This is a test INFO message, **please ignore me**! There's nothing to worry about!", MessageLevel.INFO)
        cls.send_discord_message("This is a test PLAYER ACTION REQUIRED message, **please ignore me**! There's nothing to worry about!", MessageLevel.PLAYER_ACTION_REQUIRED)
        cls.send_discord_message("This is a test ADMIN ACTION REQUIRED message, **please ignore me**! There's nothing to worry about!", MessageLevel.ADMIN_ACTION_REQUIRED)
        cls.send_discord_message("This is a test WARNING message, **please ignore me**! There's nothing to worry about!", MessageLevel.WARNING)
        return cls.send_discord_message("This is a test ERROR message, **please ignore me**! There's nothing to worry about!", MessageLevel.ERROR)

    @classmethod
    def send_email(cls, message, message_level: MessageLevel) -> MessageResponse:
        email_address = cls.application.settings_handler.email_address.get()
        smtp_server = cls.application.settings_handler.smtp_server.get()
        smtp_port = cls.application.settings_handler.smtp_port.get()
        smtp_password = cls.application.settings_handler.email_password.get()

        if is_empty_or_none([email_address, smtp_server, smtp_port, smtp_password]):
            return MessageResponse(False, MessageLevel.ADMIN_ACTION_REQUIRED, "One of the email fields is invalid")

        msg = EmailMessage()
        msg['Subject'] = "Palworld Server Manager: " + message_level.name.upper()
        msg['From'] = email_address
        msg['To'] = email_address

        msg.set_content("Message Level: " + message_level.name.upper() + "\n\n" + message)
        success = False
        server = smtplib.SMTP(smtp_server, smtp_port)

        try:
            server.connect(host=smtp_server, port=smtp_port)  # Connect to the SMTP server, might ignore response?
            server.starttls()
            server.login(email_address, smtp_password)  # Login to the email account
            server.send_message(msg, email_address, email_address)
            cls.application.append_output("Sent notification email successfully.")
            success = True
        except Exception as e:
            cls.application.append_output(f"Notification email was not sent successfully due to error: " + str(e))
            success = False
        finally:
            server.quit()
            return MessageResponse(success,
                                   MessageLevel.ALL_CLEAR if success else MessageLevel.ERROR,
                                   None if success else "Notification email was not sent successfully due to server error")

    @classmethod
    def send_test_email(cls) -> MessageResponse:
        return cls.send_email("Test Email", MessageLevel.INFO)


def is_empty_or_none(tests: list[str]):
    ret = False
    for test in tests:
        ret = ret or (test is None or test == '')
    return ret
