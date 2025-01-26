import os
import src.gui
import src.warning
# Define the path to the file in the user's directory
file_path = os.path.expanduser('~/.config/fnmanager/ignoresafetywarnings')

# Check if the file exists
if os.path.exists(file_path):
    print(file_path)
    src.gui.gui()
else:
    print(file_path)
    src.warning.main()