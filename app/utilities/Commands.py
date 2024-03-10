from app import Application


class Commands:
    def __init__(self, application: 'Application.Application'):
        self.application: Application = application
        # todo figure out how to integrate this, wire this up
        #  need to pass a lot of UI elements to get their settings?
        #  do a SettingsHandler object, pass to all elements and have them update that in real-time?
        pass

    def update_commands(self):
        pass
        try:
            arrcon_prefix = f'{self.application.settings_handler.arrcon_location.get()}/arrcon.exe -H 127.0.0.1 -P {rcon_port} -p {rcon_pass}'
            arrcon_save_server = f'{arrcon_prefix} "save"'
            arrcon_info_server = f'{arrcon_prefix} "info"'
            arrcon_shutdown = f'{arrcon_prefix} "shutdown 60 The_server_will_be_restarting_in_60_seconds"'
            arrcon_server_message_30 = f'{arrcon_prefix} "broadcast The_server_will_be_restarting_in_30_seconds"'
            arrcon_server_message_10 = f'{arrcon_prefix} "broadcast The_server_will_be_restarting_in_10_seconds"'
            shutdown_server = f'{arrcon_prefix} "shutdown 5 The_server_will_be_shutting_down_in_5_seconds"'
            force_shutdown_server = f'{arrcon_prefix} "doexit"'
            start_server = f'{palworld_directory}/PalServer.exe {server_start_args}'

            return "commands updated"
        except Exception as e:
            append_to_output(f"There was an issue creating the ARRCON commands and server startup command. Error: " + str(e))
