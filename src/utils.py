"""
FILE SCOUT
----------
file: utils.py

All helper functions live here.

"""





def user_instructions():
    """
    Prints out different command statements that are used in this programme.
    """
    print(f"-------------------------------------------")
    # Zero argument commands
    print(f"\nOne of the following commands might help:")
    # One argument commands
    print(f"\n          --- One argument commands ---")
    print(f"'q' for quit.")
    print(f"'list'                  list all files and folders.")
    print(f"'organise'              list all files organised by extension.")
    print(f"'reveal'               show all hidden files and folders")
    print(f"'scan'                  display all files and folders with details.")
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