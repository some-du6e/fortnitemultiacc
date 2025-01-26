import os
import shutil
import time

try:
    import os
    import shutil
    import time
    import tkinter
    # sybau pygame
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
    import pygame
except ImportError:
    print("Installing required modules...")
    os.system('pip install os shutil time tkinter pygame')
    print("Modules installed")

def timewaster():
    end_time = time.time() + 3
    while time.time() < end_time:
        for dot in ['  ⠋  ', '  ⠙  ', '  ⠹  ', '  ⠸  ', '  ⠼  ', '  ⠴  ', '  ⠦  ', '  ⠧  ', '  ⠇  ', '  ⠏  ']:
            print(dot, end='\r')
            time.sleep(0.1)

if os.path.exists(os.path.expanduser('~/.config/fnmanager')):
    print("do you want to reinstall? (y/n)")
    if input().lower() == 'n':
        print("ok diddy")
        exit()
    else:
        print("go run debug.py and choose 1")


print("Installing files...")
timewaster()
# Get the current folder path
current_folder = os.path.dirname(os.path.abspath(__file__))

# Define the destination path in the .config directory
destination_folder = os.path.expanduser('~/.config/fnmanager')

# Copy the current folder to the destination
shutil.copytree(current_folder, destination_folder, ignore=shutil.ignore_patterns('.git'), dirs_exist_ok=True)

print(f"Installed files to {destination_folder}")

print("adding start menu stuff")
timewaster()
