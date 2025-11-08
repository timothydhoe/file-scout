# File Scout (FS-26)

*Interactive REPL for hands-on file exploration.*
Rediscover what's hiding in your file system.

**status**: In active development. I'm sure this document will make more sense in the future 😝*

## What it does

File Scout lets you explore directories with retro CP/M-style commands and uncover patterns you didn't know existed:
<!-- The patterns that we didn't know existed sounds very data analyst-like. How to implement some machine learning or other analysis in here? -->
- Navigate folders with classic commands (DIR, TYPE, ERA)
- Use wildcards to filter files (`*.py`, `README.*`)
- Bookmark frequently-used paths (A:, B:, C:)
- Find forgotten files, size hogs, and temporal patterns
- Analyze folder structures without leaving the command line

## Getting started

```bash
cd file-scout
python3 src/main.py
```

<!-- This option might be removed in future versions and just start the REPL in the cwd. -->
Choose your starting directory (Current or Home), then explore!

## Command Syntax

File Scout uses **CP/M-style syntax** for that vintage computing feel:
```bash
COMMAND [filespec] [marker:] [parameters]
```

**Examples:**
```bash
DIR                # List all files
DIR *.py           # Show only Python files
DIR A:*.txt        # Show .txt files from marker A:
TYPE readme.md     # Display file contents
ERA oldfile.pdf    # Delete a file
```

**Command Components:**
- `COMMAND` - The action (DIR, TYPE, ERA, STAT)
- `filespec` - Filename or pattern with wildcards (`*.txt`, `file?.py`)
- `marker:` - Quick access to saved paths (A:, B:, C:)
- `parameters` - Options in brackets `[V]`, `[B]`

## Currently Implemented

- [x] DIR - List files with wildcard(*) support
- [x] File/folder navigation
- [x] File information display
- [ ] TYPE - Display file contents
- [ ] ERA - Delete files
- [ ] Marker management (A:, B:, C:)
- [ ] PIP - File operations
- [ ] Discovery insights (size hogs, forgotten files, etc.)


## CP/M Operating System Inspiration

**CP/M** (Control Program for Microcomputers) was a pioneering OS from the 1970s-80s that influenced MS-DOS and modern command-line interfaces.

File Scout takes inspiration from CP/M's elegant command syntax and file management philosophy.

**Learn more:**
- [CP/M on Wikipedia](https://en.wikipedia.org/wiki/CP/M)
- [CP/M-86 Command Summary](http://www.cpm.z80.de/randyfiles/DRI/CPM-86_Command_Summary.pdf)
- [PIP (Peripheral Interchange Program)](https://en.wikipedia.org/wiki/Peripheral_Interchange_Program)
- [Epson PX-8 CP/M Manual](https://vintagecomputer.net/epson/PX-8/px8-BASIC.pdf)


## Built With

Python 3 | `os` module | `datetime`


## Why This Project?

Built to practice Python fundamentals (classes, dicts, lists, functions, file I/O) while creating something genuinely useful and fun. Combines technical learning with computing history appreciation.


## License

MIT License. I think.




## Future: Data Analysis & Insights

*Coming later, after core commands are working properly!*

File Scout will eventually apply **data science techniques** to help you understand your file system:

**Pattern Discovery**
- Detect file naming conventions and habits
- Identify creation time patterns
- Analyze size distributions and anomalies

**ML-Powered Features**
- Duplicate detection with fuzzy matching
- File clustering by similarity
- Anomaly detection (suspicious files)
- Auto-categorization suggestions

**Temporal Analysis**
- Track file system evolution over time
- Predict disk space trends
- Identify workflow patterns