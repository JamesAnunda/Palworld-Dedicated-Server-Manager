import webbrowser


def get_or_default(val, default):
    return val if val != "" else default

def open_discord(event):
    webbrowser.open("https://discord.gg/bPp9kfWe5t")

def open_BMAB(event):
    webbrowser.open("https://www.buymeacoffee.com/thewisestguy")

def check_for_updates():
    webbrowser.open("https://github.com/Andrew1175/Palworld-Dedicated-Server-Manager/releases")

def report_bug():
    webbrowser.open("https://github.com/Andrew1175/Palworld-Dedicated-Server-Manager/issues")
