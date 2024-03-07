import os
import sys

from app.Application import Application


def run():
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the PyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app
        # path into variable _MEIPASS'. This _WILL_ show a warning in an IDE
        root_path = sys._MEIPASS
    else:
        root_path = os.path.dirname(os.path.abspath(__file__))

    app = Application(root_path=root_path)
    app.mainloop()


if __name__ == "__main__":
    run()
