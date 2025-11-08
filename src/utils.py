"""
FILE SCOUT
----------
file: utils.py

All helper functions live here.

"""

def matches_pattern(filespec, pattern):
    """
    Match filename against pattern with wildcards (* and ?)

    TODO: add "<", ">", ":"
    """
    filespec = filespec.upper()
    pattern = pattern.upper()

    # handle not pattern first?
        # -> eg. text_here.txt
    if "*" not in filespec:
        return None
        
    # if '*' in filespec:
        # if '*.' -> check filename extension. [pos *:]
        # elif -> '.*' -> check filename

    # if '?' in filespec:
        # replace '?' with any character.




def user_instructions():
    """
    Prints out different command statements that are used in this programme.
    """
    print("\n" + "="*50)
    print(f"FILE SCOUT - CP/M COMMAND REFERENCE")
    print("="*50)

    print(f"\n📂 FILE OPERATIONS")
    print("  DIR")
    print("  DIR *.py")
    print("'list'                  list all files and folders.")
    print("'organise'              list all files organised by extension.")
    print("'reveal'               show all hidden files and folders")
    print("'scan'                  display all files and folders with details.")
    print(f"'where am i'            print the current working directory")
    # Multiple argument commands
    print(f"\n        --- Multiple argument commands ---")
    print(f"'enter <foldername>'   navigate inside the folder")
    print(f"'info folder'          more information on the folder structure.")
    print(f"'info file'            more information on the file.\n")


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