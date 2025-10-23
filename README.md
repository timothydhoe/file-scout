# File Scout

The programme that helps users become more 🫶 **intimate** 🫶 with their files and folders.

## What It Does

File Scout lets you explore directories and uncover their dirtiest secrets:
- See what file types dominate your folders
- Find forgotten files and size hogs
- Track when files were last touched
- Navigate and analyse without leaving the command line

## Getting Started

```
cd file-scout
python3 src/main.py
```
Choose your starting directory, then explore with simple commands.

## Commands

**Navigation**
- `list` - Show files and folders in current directory
- `change <folder>` - Move into a folder
- `where am i` - Show current location

**Discovery**
- `scan` - display all files and folders with details.
- `info file` - Detailed file information
- `info folder` - Detailed information on the folder structure.

**Other**
- `help` - Show available commands
- `q` - Quit


## Built With

Python 3 + `os` module + `datetime`

## Inspiration

This project was inspired by basic commandline functions and python's `os` module.
Built to practice Python fundamentals (dicts, lists, functions) while creating something genuinely fun for understanding your file system.


## License

MIT License.