from app import Application


class Commands:
    def __init__(self, application: 'Application.Application'):
        self.application: Application = application
        self.arrcon_save_server = ""
        self.arrcon_info_server = ""
        self.arrcon_shutdown = ""
        self.arrcon_server_message_30 = ""
        self.arrcon_server_message_10 = ""
        self.shutdown_server = ""
        self.force_shutdown_server = ""
        self.start_server = ""

    def update_commands(self):
        pass
        try:
            arrcon_prefix = f'{self.application.settings_handler.arrcon_location.get()}/arrcon.exe -H 127.0.0.1 -P {self.application.settings_handler.rcon_port.get()} -p {self.application.settings_handler.rcon_pass.get()}'
            self.arrcon_save_server = f'{arrcon_prefix} "save"'
            self.arrcon_info_server = f'{arrcon_prefix} "info"'
            self.arrcon_shutdown = f'{arrcon_prefix} "shutdown 60 The_server_will_be_restarting_in_60_seconds"'
            self.arrcon_server_message_30 = f'{arrcon_prefix} "broadcast The_server_will_be_restarting_in_30_seconds"'
            self.arrcon_server_message_10 = f'{arrcon_prefix} "broadcast The_server_will_be_restarting_in_10_seconds"'
            self.shutdown_server = f'{arrcon_prefix} "shutdown 5 The_server_will_be_shutting_down_in_5_seconds"'
            self.force_shutdown_server = f'{arrcon_prefix} "doexit"'
            self.start_server = f'{self.application.settings_handler.palworld_location.get()}/PalServer.exe {self.application.settings_handler.server_start_args.get()}'

            return "commands updated"
        except Exception as e:
            self.application.append_output(f"There was an issue creating the ARRCON commands and server startup command. Error: " + str(e))
