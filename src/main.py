"""
FILE SCOUT
----------
file: main.py

Programme that helps users become more intimate with their files and folders.

"""

from datetime import datetime
import os


def main():
    """
    Programme asks user for starting directory.
    From there, it proposes a couple of actions to move directory,
    retrieve file information, etc.
    """

    # Define variables
    cwd = os.getcwd()	# Directory
    instruct = ""		# User instructions

    # Define user starting directory
    print_title()
    
    print(f"\nYou are currently at:\n\t👉 {cwd}\n")
    print("")
    user_dir = initiate_directory(cwd)
    
    # Main user control flow
    while True:
        instruct = []
        instruct = user_command()
        
        # Zero arguments
        if instruct[0] == "":
            user_instructions()

        # One arguments
        if len(instruct) == 1:
            if instruct[0] == 'q' or instruct[0] == 'quit':
                print(f"\nBye bye... 👋\n")
                break

            if instruct[0] == "list":
                print()
                show_files_and_folders(user_dir)

            if instruct[0] == "help":
                print(f"\nI don't know where I am or what my purpose in life is, but at least I have you... 👀\n")

            if instruct[0] == 'scan':
                scan_directory(user_dir)

            # TODO: add order by extension

        # Multiple arguments
        if len(instruct) > 1:
            if instruct[0] == "change":
                if not instruct [1]:
                    print(f"usage: 'change <DIRECTORY>'")
                elif instruct[1] == "..":
                    # TODO: go up one folder
                    pass
                else:
                    next_dir = instruct[1]
                    change_directory(user_dir, next_dir)
        

            if instruct[0] == "info" and instruct[1] == "folder":
                # if sys.arg[1] is a folder indeed:
                show_folders(user_dir)
                foldername = input("which folder?")
                get_folder_info(user_dir)
                # TODO: write and add function (like file_info)

            if instruct[0] == "info" and instruct[1] == "file":
                show_files(user_dir)
                filename = input("what file? ")
                # TODO: raise warning/error when file not present
                file_info = get_file_info(os.path.join(user_dir, filename))
                print_dict(file_info)

            if instruct[0] == "where" and instruct[1] == "am" and instruct[2] == "i":
                pass
                # os.getcwd()

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
            cwd = os.environ['HOME']
            break
        elif user_input.lower() == 'c':
            return cwd
        else:
            print("Type 'C' to remain at your current directory.")
            print("Type 'H' to go to your HOME directory.\n")

    print(f"\nYou are currently at:\n\t👉 {cwd}\n")
    print(f"Ready to explore the files and folders?")
    print(f"Type 'help' to see more commands.\n")
    return cwd


def user_instructions():
    """
    Prints out different command statements that are used in this programme.
    """
    print(f"-------------------------------------------")
    # Zero argument commands
    print(f"\nOne of the following commands might help:")
    # One argument commands
    print(f"\n--- One argument commands ---")
    print(f"'q' for quit.")
    print(f"'list' to list all files and folders.")
    print(f"'scan' to deep dive into your folder structure.")
    # Multiple argument commands
    print(f"\n--- Multiple argument commands ---")
    print(f"'change <foldername>' to navigate inside the folder")
    print(f"'info <foldername>' to get more information on the folder.")
    print(f"'info <filename>' to get more information on the file.\n")


def user_command():
    """
    Takes strings as user input.
    Returns a list with command keywords.
    """
    commands_list = []
    tmp_cmd = ""

    print(f"What would you like to do?")
    user_input = input("cmd: ")
    for i in user_input.lower():
        if i.isalpha():
            tmp_cmd += i
        # in case of space (multiple commands)
        elif i.isspace():
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
    folder_info_dict = {}
    file_info_dict = {}

    folders, files = show_files_and_folders(path)
    print("\n📂 Folders:")
    if not folders:
        print(f"No folders to display.\n")
    else:
        for folder in folders:
            folder_info_dict = get_folder_info(os.path.join(path, folder))
            print_dict(folder_info_dict)

    print("\n📑 Files:")
    if not files:
        print(f"No files to display.\n")
    else:
        for file in files:
            file_info_dict = get_file_info(os.path.join(path, file))
            print_dict(file_info_dict)

    # return folders_info_dict, files_info_dict


def show_files_and_folders(path):
    """
    Takes a directory path and prints two lists containing files and folders.
    Returns two lists of both folders and files.
    """
    folders = [item for item in os.listdir(path)
               if os.path.isdir(os.path.join(path, item)) and not item.startswith('.')]
    files = [item for item in os.listdir(path)
             if os.path.isfile(os.path.join(path, item)) and not item.startswith('.')]

    print("\n📂 Folders:")
    for f in folders:
        print(f"/{f}", end="\t")
    print()
    print("\n📑 Files:")
    for f in files:
        print(f"{f}", end="\t")
    print()
    
    return folders, files


def get_folder_info(folderpath):
    # TODO
    """
    Takes a folderpath.
    Returns a dict with path, size and last modified information.
    """
    stats = os.stat(os.path.join(folderpath))
    date = datetime.fromtimestamp(stats.st_mtime)

    return {
        'path': folderpath,
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


def show_files(path):
    """
    Takes a directory path and prints two lists containing files and folders.
    Returns two lists of both folders and files.
    """
    files = [item for item in os.listdir(path)
             if os.path.isfile(os.path.join(path, item)) and not item.startswith('.')]

    print("\n📑 Files:")
    for f in files:
        print(f"  {f}")
    print("")
    
    return files


def show_folders(path):
    """
    Takes a directory path and prints two lists containing files and folders.
    Returns two lists of both folders and files.
    """
    folders = [item for item in os.listdir(path)
               if os.path.isdir(os.path.join(path, item)) and not item.startswith('.')]

    print("📂 Folders:")
    for f in folders:
        print(f"  {f}")
    print("\n📑 Files:")
    
    return folders


def files_by_type(filepath):
    # TODO: 
    """ Organise files by extension in dictionary

    files_by_type = {
        ".jpg": [
            {'path': 'path/name.jpg', 'size': '1024MB', 'modified': '...' },
            {'path': 'path/name.jpg', 'size': '1024MB', 'modified': '...' },
        ]
        ".pdf": [
            {'path': 'path/name.pdf', 'size': '1024MB', 'modified': '...' },
            {'path': 'path/name.pdf', 'size': '1024MB', 'modified': '...' },
        ]
    }
    """
    pass

def change_directory(path, dir_name):
    os.chdir(os.path.join(path,dir_name))
    return f"you've moved to {os.path.join(path,dir_name)}"


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

def organise_by_extenstion(file_list):
    # TODO: organise output by extension
    """ organise_by_extenstion(file_list)
        takes list from scan_directorty and groups files by extension
    """
    pass

def print_title():
    """
    Prints the File Scout ASCII art title.
    """
    print(r"""
      ______ _ _         _____                 _   
     |  ____(_) |       / ____|               | |  
     | |__   _| | ___  | (___   ___ ___  _   _| |_ 
     |  __| | | |/ _ \  \___ \ / __/ _ \| | | | __|
     | |    | | |  __/  ____) | (_| (_) | |_| | |_ 
     |_|    |_|_|\___| |_____/ \___\___/ \__,_|\__|
                                       
    """)
    print(f"The programme to get more intimate with your files and folders.\n")

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