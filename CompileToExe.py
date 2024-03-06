from pathlib import Path

import PyInstaller.__main__


def compile_to_exe():
    """
    Equivalent to:
        pyinstaller --clean --noconfirm --onefile --windowed --icon "./palworld_logo.ico"
        --name "PalWorldServerManager" --add-data "./version.txt;." --add-data "./palworld_logo.ico;.
        --distpath "./ouput" --workpath "./build" ./Driver.py"
    """
    PyInstaller.__main__.run([
            '--clean', '--noconfirm',
            '--onefile', '--windowed',
            '--icon=palworld_logo.ico',
            '--name=PalWorldServerManager',
            '--add-data=version.txt;.',
            '--add-data=palworld_logo.ico;.',
            '--distpath=output',
            '--workpath=build',
            'Driver.py'
    ])

def rmdir(directory):
    directory = Path(directory)
    for item in directory.iterdir():
        rmdir(item) if item.is_dir() else item.unlink()
    directory.rmdir()


if __name__ == "__main__":
    compile_to_exe()
    rmdir("build")
