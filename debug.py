import os
import shutil

hawktuah = input("debug")
if hawktuah == "1":
    config_path = os.path.expanduser('~/.config/fnmanager')
    if os.path.exists(config_path):
        shutil.rmtree(config_path)
        print(f"Removed {config_path}")
    else:
        print(f"{config_path} does not exist")