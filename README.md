# File Scout (FS-26)

The programme that helps users become more 🫶 **intimate** 🫶 with their files and folders.

*This project is still in research/development stage.*


## TODO

1. Make TODO.md to keep track of changes.
2. replace commands with original CP/M-86 commands.


Change commands to original CP/M-86 Commands.
[List of commands here.](https://vintagecomputer.net/epson/PX-8/px8-BASIC.pdf)

[PIP Commands](https://en.wikipedia.org/wiki/Peripheral_Interchange_Program)



## CP/M Operating System as inspiration

If you don't know what CP/M is and what it stands for I recommend a short read on [Wikipedia here](https://en.wikipedia.org/wiki/CP/M).

A more in depth document of the OG Operating System can be found [here](http://www.cpm.z80.de/randyfiles/DRI/CPM-86_Command_Summary.pdf).


## What It Does

TODO: update with new direction
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