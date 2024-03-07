from app import Application


class Commands:
    def __init__(self, application: 'Application.Application'):
        self.application: Application = application
        # todo figure out how to integrate this, wire this up
        pass

    def update_commands(self):
        pass
        # try:
        #     arrcon_exe_path = f'{arrcon_directory_selection.cget("text")}/ARRCON.exe'
        #     rcon_getport = rcon_port.cget("text")
        #     palworld_directory = server_directory_selection.cget("text")
        #     server_start_args = server_start_args_entry.get()
        #     arrcon_command_save_server = f'{arrcon_exe_path} -H 127.0.0.1 -P {rcon_getport} -p {rcon_pass} "save"'
        #     arrcon_command_info_server = f'{arrcon_exe_path} -H 127.0.0.1 -P {rcon_getport} -p {rcon_pass} "info"'
        #     arrcon_command_shutdown_server = f'{arrcon_exe_path} -H 127.0.0.1 -P {rcon_getport} -p {rcon_pass} "shutdown 60 The_server_will_be_restarting_in_60_seconds"'
        #     arrcon_command_server_message_30 = f'{arrcon_exe_path} -H 127.0.0.1 -P {rcon_getport} -p {rcon_pass} "broadcast The_server_will_be_restarting_in_30_seconds"'
        #     arrcon_command_server_message_10 = f'{arrcon_exe_path} -H 127.0.0.1 -P {rcon_getport} -p {rcon_pass} "broadcast The_server_will_be_restarting_in_10_seconds"'
        #     start_server_command = f'{palworld_directory}/PalServer.exe {server_start_args}'
        #     shutdown_server_command = f'{arrcon_exe_path} -H 127.0.0.1 -P {rcon_getport} -p {rcon_pass} "shutdown 5 The_server_will_be_shutting_down_in_5_seconds"'
        #     force_shutdown_server_command = f'{arrcon_exe_path} -H 127.0.0.1 -P {rcon_getport} -p {rcon_pass} "doexit"'
        #     return "commands updated"
        # except Exception as e:
        #     append_to_output(f"There was an issue creating the ARRCON commands and server startup command. Error: " + str(e))
