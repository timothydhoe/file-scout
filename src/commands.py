"""
FILE SCOUT
----------
file: commands.py

Holds all the command functions

cwd = current working directory
nwd = working directory

"""

def execute_command(user_input):
    pass
    # Map to existing functions
    # DIR -> show_files_and_folders()
    # STAT -> get_file_info()
    # ...

def cmd_dir(cwd, cmd):
    """Execute DIR command. lists all files in directory."""
    folders = [item for item in os.listdir(path)
               if os.path.isdir(os.path.join(path, item)) and not item.startswith('.')]
    files = [item for item in os.listdir(path)
             if os.path.isfile(os.path.join(path, item)) and not item.startswith('.')]

    return folders, files

def cmd_cd(cwd, nwd, cmd):
    """"Execute the CD command. Navigation logic.""""
    pass

def cmd_era(cwd, cmd):
    """Execute ERA command. Delete files."""
    pass

def cmd_type(cwd, cmd):
    """Execute TYPE command. Display file info."""
    pass