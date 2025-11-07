"""
FILE SCOUT
----------
file: main.py

Programme (REPL) that helps users become more intimate with their files and folders.

"""

from datetime import datetime
import os

from parser import Command
import utils

"""
# TODO: Cleanup (dirs vs files) naming
# TODO: cleanup variable naming

# A CP/M-86 command line is composed of a command, an optional command tail, and a carriage return.
# The COMMAND identifies a command(programme) to be executed.
COMMANDS = ['DIR', 'ERA', 'SAVE', 'TYPE', 'USER', 'CONFIG', 'FILINK', 'PIP', ]
# PIP, or Peripheral Interchange Commands, was a utility to transfer files on and between devices on Digital Equipment Corporation's computers.
PIP_PARAMETERS = ['[B]', '[Dn]', '[E]', '[F]', '[Gn]', '[R]', '[V]', '[W]']
# The optional command TAIL can consist of a drive specification, one or more file specifacations, and some options or parameters.
TAILS = []
# A carriage return is needed to complete the command.
RETURN ['\n']
# Special symbols can be sued to define command syntax.
SYMBOLS = ['{','}',, '|','<cr>', 'RW', 'RO', 'SYS', 'DIR'. '*', '?']
"""

def main():
    """
    REPL (Read-Eval-Print Loop) for File Scout.
    
    Asks user for starting directory, then provides an interactive
    CP/M-style command interface for exploring files and folders
    """

    # Define variables
    cwd = os.getcwd()	# Directory
    instruct = ""		# User instructions

    # Define user starting directory
    utils.print_title()
    
    print(f"\nYou are currently at:\n\t👉 {cwd}\n")
    print("")
    # Remove this option and just start in cwd?
    cwd = initiate_directory(cwd)
    
    # Main user control flow
    while True:
        user_input = input("cmd >>> ")
        cmd = Command.input_to_cmd(user_input)

        if cmd.command == "":
            utils.user_instructions()

        elif cmd.command == "Q" or cmd.command == "QUIT":
            print(f"Bye bye... 👋")
            os._exit(0)

        elif cmd.command == "DIR":
            folders, files = show_files_and_folders(cwd)

        elif cmd.command == "TYPE":
            # Display file contents
            pass

        elif cmd.command == "ERA":
            # Delete files
            pass

        elif cmd.command == "STAT":
            # Display file stats
            # TODO: needs fixing...
            pass
            # folders = get_folder_info()
            # files = get_file_info()

        # User File management
        elif cmd.command == "CD":
            pass
            # change directory
        elif cmd.command == "MV":
            pass
            # Move file
            # [R] parameter needed for recursive? Folders.
        elif cmd.command == "CD":
            pass
            # change directory


        print_files_and_folders(folders, files)

        # TODO: add other commands (TYPE, ERA, STAT, etc.)


"""
I'm using the functions below still and I will slowly transition out of them, I'm sure.
The plan is to clean this up slowly as the programme starts to make more sense in my head. 
"""

#
# Functions
#
def initiate_directory(cwd):
    """
    Function gets called when the programme starts.
    Returns Directory of user's choice.
    """
    print("What would you like to do?")
    print("Type 'C' to remain at your current directory.")
    print("Type 'H' to go to your HOME directory.\n")
    while True:
        user_input = input("directory: ")

        if user_input.lower() == 'h':
            cwd = os.path.expanduser('~')
            break
        elif user_input.lower() == 'c':
            cwd = cwd
            break
        else:
            print("Type 'C' to remain at your current directory.")
            print("Type 'H' to go to your HOME directory.\n")

    print(f"\nYou are currently at:\n\t👉 {cwd}\n")
    return cwd
    # print(f"Ready to explore the files and folders?")
    # print(f"Type 'help' to see more commands.\n")


def user_command():
    """
    Takes strings as user input.
    Returns a list with command keywords.
    """
    commands_list = []
    tmp_cmd = ""

    # print(f"What would you like to do?")
    user_input = input("cmd >>> ")
    for i in user_input.lower():
        if not i.isspace():
            tmp_cmd += i
        else:
            commands_list.append(tmp_cmd)
            tmp_cmd = ""

    commands_list.append(tmp_cmd)
    return commands_list


def scan_directory(path):
    """ 
    Takes a path as input, calls get_file_info() on every file found.
    Prints out folder and file information.

    Returns two dicts of folders and files.
    """
    folders_info_dict = {}
    files_info_dict = {}

    folders, files = show_files_and_folders(path)
    print("\n📂 Folders:")
    if not folders:
        print(f"No folders to display.\n")
    else:
        for folder in folders:
            folders_info_dict = get_folder_info(os.path.join(path, folder))
            print_dict(folders_info_dict)

    print("\n📑 Files:")
    if not files:
        print(f"No files to display.\n")
    else:
        for file in files:
            files_info_dict = get_file_info(os.path.join(path, file))
            print_dict(files_info_dict)

    return folders_info_dict, files_info_dict


def show_files_and_folders(path):
    """
    Takes a directory path and prints two lists containing files and folders.
    Returns two lists of both folders and files.
    """
    folders = [item for item in os.listdir(path)
               if os.path.isdir(os.path.join(path, item)) and not item.startswith('.')]
    files = [item for item in os.listdir(path)
             if os.path.isfile(os.path.join(path, item)) and not item.startswith('.')]

    return folders, files

def reveal_files_and_folders(path):
    """
    Takes a directory path and prints two lists containing files and folders.
    Returns two lists of both folders and files.
    """
    folders = [item for item in os.listdir(path)
               if os.path.isdir(os.path.join(path, item))]
    files = [item for item in os.listdir(path)
             if os.path.isfile(os.path.join(path, item))]

    return folders, files

def print_files_and_folders(folders, files):
    """
    FILL IN
    """
    print("\n📂 Folders:")
    if not folders:
        print(f"No folder to display.\n")
    else:
        for f in folders:
            print(f"/{f}", end="\t")
        print()

    print("\n📑 Files:")
    if not files:
        print(f"No files to display.\n")
    else:
        for f in files:
            print(f"{f}", end="\t")
        print("\n\n")

def get_folder_structure(folder):
    """
    Returns a dict with path, size and last modified information.
    """
    stats = os.stat(os.path.join(folder))
    date = datetime.fromtimestamp(stats.st_mtime)

    dir_counter = 0
    file_counter = 0
    # Travers all the branches of the selected folder.
    for (root, dirs, files) in os.walk(os.path.join(folder), topdown=True):
        # TODO: add up sizes to display a grand total
        print(f"Path: {root}")
        print(f"\t📂 Folders:")
        print_list(dirs)
        print("\n\t📑 Files:")
        print_list(files)
        print("---\n")

    # Return only useful info.
    return {
        'path': folder,
        'size': format_size(stats.st_size),
        'modified': date.strftime("%Y-%m-%d %H:%M:%S"),
    }


def get_folder_info(folder):
    """
    Returns a dict with path, size and last modified information.
    """
    stats = os.stat(os.path.join(folder))
    date = datetime.fromtimestamp(stats.st_mtime)

    # Return only useful info.
    return {
        'path': folder,
        'size': format_size(stats.st_size),
        'modified': date.strftime("%Y-%m-%d %H:%M:%S"),
    }


def get_file_info(filepath):
    """
    Take the path of a file and outputs size, last modified and the extension.
    Returns a dict.
    """
    stats = os.stat(filepath)
    extention = os.path.splitext(filepath)
    date = datetime.fromtimestamp(stats.st_mtime)

    return {
        'path': filepath,
        'size': format_size(stats.st_size),
        'modified': date.strftime("%Y-%m-%d %H:%M:%S"),
        'ext': extention[-1].upper(),
    }


def show_folders(path):
    """
    Takes a directory path and prints a list of folders.
    Returns a list of the names of the folders.
    """
    folders = [item for item in os.listdir(path)
               if os.path.isdir(os.path.join(path, item)) and not item.startswith('.')]

    print("📂 Folders:")
    if not folders:
        print(f"\tThere are no folders in {path}\n")
    else:
        for f in folders:
            print(f"\t{f}")
        print("\n")
    
    return folders


def show_files(path):
    """
    Takes a directory path and prints a list of files.
    Returns a list containing the names of the files.
    """
    files = [item for item in os.listdir(path)
             if os.path.isfile(os.path.join(path, item)) and not item.startswith('.')]

    print("\n📑 Files:")
    if not files:
        print(f"\tThere are no files in {path}\n")
    else:
        for f in files:
            print(f"\t{f}")
        print("\n")
    
    return files


def change_directory(path, dir_name):
    new_path = os.path.join(path, dir_name)
    return new_path


def organise_by_extention(filepath):
    """
    Takes a dict of files
    Returns a list of files in cwd, organised by extention.
    """
    folders, files = show_files_and_folders(filepath)
    for file in files:
        print_dict(get_file_info(os.path.join(filepath, file)))
    # print(labeled_files)

#
# Helper Functions
#
def format_size(size_in_bytes):
    """
    Transforms general output in bytes into readable sizes.
    Returns size in KB, MB or GB.
    """
    if size_in_bytes >= (1_024 ** 3):
        return f"{size_in_bytes / (1_024 ** 3):.2f} GB"
    elif size_in_bytes > (1_024 ** 2):
        return f"{size_in_bytes / (1_024 ** 2):.2f} MB"
    elif size_in_bytes > 1_024:
        return f"{size_in_bytes / 1_024:.2f} KB"
    else:
        return f"{size_in_bytes} bytes"

def print_dict(dict):
    """
    Takes a dictionary and prints out the key and corresponding values.
    Returns None.
    """
    for key, value in dict.items():
        print(f"{key}: {value}")
    print()

def print_list(list):
    """
    Takes a list as input and prints it out.
    """
    if not list:
        print(f"\tNothing found.")
    else:
        for i in list:
            print(f"\t{i}")



#
# Run the programme
#
if __name__ == "__main__":
    main()




"""
print(os.chdir('path'))				# change dir
print(os.getcwd())					# get current working dir
print(os.listdir('path'))			# get list of files and folders

os.mkdir('')						# make dir
os.mkdirs('')						# make nested dirs

os.rmdir							# remove dir
os.removedirs						# remove dirs, nested

os.rename('og_name.txt' 'new_name.text')		# rename file

os.stat(<filename>)             	# print all info of a file
    --> .st_size (in bytes)
    -->	.st_mtime (modification time)

os.walk(<path>)	                	# traverse directory recursively
for dirpath, dirnames, filenames in os.walk(r'/Users/timothydhoe/Syntra'):
    print(f"Current path: {dirpath}")
    print(f"directories: {dirnames}")
    print(f"files: {filenames}")
    print("\n\n\n")

os.environ							# get environment variables

os.path.join(<path>, <file>)		# join path without worrying about /

os.path.basename(<filename>)		# get basename
os.path.dirname(<filename>)			# get dirname
os,path.split('path/filename')		# gives both

os.path.exists(<path-to-file>)		# check if the path exists or not
os.path.splitext(<path-to-file>)	# split path and file extension
dir(os)								# check what methods exists

"""