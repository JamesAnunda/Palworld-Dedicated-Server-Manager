import os

from views.Application import Application


def run():
    root_path = os.path.abspath(os.path.dirname(__file__))
    app = Application(root_path=root_path)
    app.mainloop()


if __name__ == "__main__":
    run()
