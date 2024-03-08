import datetime
import time
import webbrowser

import requests

from app import Application


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

    @classmethod
    def send_discord_message(cls, message, is_problem):
        message = message\
            if (message is not None and message != '')\
            else ('This message indicates that the PalWorld Server was not running. '
                  'No worries though, the server was restarted and is back online. Beep beep boop.')
        current_time = datetime.datetime.now().replace(microsecond=0)
        message = "Sent at your local time: <t:" + str(int(time.mktime(current_time.timetuple()))) + ">\n" + message
        discord_webhook = cls.application.settings_handler.discord_webhook.get()
        if discord_webhook is None or discord_webhook == '':  # todo: further validation?
            # todo do a popup here, the webhook isn't good ... somehow
            return

        error_color = 0xFF0000
        all_good_color = 0x00FF00
        try:
            payload = {
                    "embeds": [{
                            "title":       "PalServer Manager",
                            "description": message,
                            "color":       error_color if is_problem else all_good_color
                    }]
            }
            response = requests.post(discord_webhook, json=payload)
            response.raise_for_status()  # Check for HTTP errors
            cls.application.append_output(f'Discord alert was sent: {message}')
        except requests.exceptions.RequestException as e:
            cls.application.append_output(f"Error sending Discord alert: {e}\nIntended Discord message: {message}\nDiscord Webhook URL: {discord_webhook}")

    @classmethod
    def send_test_discord_message(cls):
        cls.send_discord_message("This is a test message, **please ignore me**! There's nothing to worry about!", False)
        cls.send_discord_message("This is a test error message, **please ignore me**! There's nothing to worry about!", True)

    @classmethod
    def send_email(cls, message):
        pass

    @classmethod
    def send_test_email(cls):
        pass
