"""
FILE SCOUT
----------
file: utils.py

All helper functions live here.

"""

import os

WILDCARD_TOKENS = ['*', '?', '>'] # TODO: finish list gradually


# TODO: Should this be handled in the class Command?
def matches_pattern(filespec):  # add cwd to arguments.
    """
    Match filename against pattern with wildcards (* and ?)

    TODO: add "<", ">", ":"
    """
    cwd = os.getcwd()
    filespec = filespec.upper()
    wildcard = ""

    # other solution than looping?
    for token in WILDCARD_TOKENS:
        if token in filespec:
            wildcard = token
        
    # when token found:
    if wildcard:
        # TODO: Also handle doubles ->(FILENAME.svg.jpg)
        filename, extension = filespec.split('.')
        file_list = []
        if filename == "*":
            # TODO: Returns all files -> only return with extension.
            for item in os.listdir(cwd):
                ext_check = item.split(".")
                if ext_check[-1].upper() == extension:
                    file_list.append(item)
                
        if file_list:
            return file_list
        else:
            return f"No items found with extension .{extension}"
        # return [item for item in os.listdir(cwd) if item.split(".")]
        

        if '*' in filespec:
            pass
                
        if '*.' in filespec:
            pass
            # find position of '.'

    # if '*' in filespec:
        # if '*.' -> check filename extension. [pos *:]
        # elif -> '.*' -> check filename

    # if '?' in filespec:
        # replace '?' with any character.

print(matches_pattern("hello_world.py")) # -> None
print(matches_pattern("hello_world.*")) # -> None
print(matches_pattern("*.md")) # -> print list of all .md
print(matches_pattern("*.txt")) # -> print list of all .txt


def user_instructions():
    """
    Prints out different command statements that are used in this programme.
    """
    print("\n" + "="*50)
    print(f"FILE SCOUT - CP/M COMMAND REFERENCE")
    print("="*50)

    print(f"\n📂 FILE OPERATIONS")
    print("  DIR                    List all files and folders")
    print("  DIR *.py               List files matching pattern")
    # TODO: Add more commands.



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