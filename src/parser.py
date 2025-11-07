"""
FILE SCOUT
----------
file: scanner.py

Programme that helps users become more intimate with their files and folders.

"""


"""
- [ ] Start with just recognizing commands: DIR, TYPE, ERA, STAT
- [ ] -> simple arguments: TYPE filename.txt
- [ ] -> wildcards: DIR *.py
- [ ] -> parameters: DIR [V]
- [ ] Then ???
"""

class Command:
    def __init__(self, command, filespec=None, marker=None, parameters=None):
        self.command = command
        self.filespec = filespec
        self.marker = marker
        self.parameters = parameters

    def __repr__(self):
        return f"Command(cmd={self.command}, file={self.filespec}, marker={self.marker}, para={self.parameters})"


def parse_command(user_input):
    """
    parse CP/M-style commands
    Examples:
        "DIR"            → show all files
        "DIR *.txt"      → show .txt files
        "DIR A:*.py"     → show .py files from drive A:
        "TYPE readme.md" → display file
        "ERA old.pdf"    → delete file
    """
    # Create list of user input
    tokens = user_input.strip().upper().split()
    
    command = components[0] if components else ""
    filespec = None
    # bookmark = None
    parameter = []
    
    # Parse tokens
    for token in tokens[1:]
        # if token starts with [ and ends with ]:
            #-> parameter
        # elif : in token
            #-> what does it do/mean?
        # else:
            filespec = token

    return {
        'command': command,
        'args': arguments
    }
    # Split into command and arguments
    # Handle wildcards, drive letters, parameters
    # Return structured command dict


def execute_command(user_input):
    pass
    # Map to existing functions
    # DIR -> show_files_and_folders()
    # STAT -> get_file_info()
    # ...


