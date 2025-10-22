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

	# Main user control flow 
	print(f"\nYou are currently at:\n\t👉 {cwd}\n")
	print("")

	user_dir = initiate_directory(cwd)
	
	while True:
		instruct = []
		instruct = user_command()
		
		# Zero arguments
		if len(instruct) == 0:
			print(f"Cowboy...")
			user_instructions()

		# One arguments
		if len(instruct) == 1:
			if instruct[0] == 'q' or instruct[0] == 'quit':
				print(f"\nBye bye... 👋\n")
				break

			if instruct[0] == "ls":
				print()
				show_files_and_folders(user_dir)

			if instruct[0] == "help":
				print(f"\nI don't know where I am or what my purpose in life is, but at least I have you... 👀\n")
				user_instructions()

			if instruct[0] == 'scan':
				scan_directory(user_dir)

		# Multiple arguments
		if len(instruct) >= 2:
			if sys.arg[0] == "cd":
				#TODO: add and write function
				pass
		
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


#
# Functions
#
def initiate_directory(cwd):
	print("What would you like to do?")
	print("Type 'C' to remain at your current directory.")
	print("Type 'H' to go to your HOME directory.\n")
	while True:
		user_input = input("Input: ")

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
	# Zero argument commands
	print(f"Type nothing to be insulted... \n")
	# One argument commands
	print(f"\n--- One argument commands ---")
	print(f"'q' for quit.")
	print(f"'ls' to list all files and folders.")
	print(f"'scan' to deep dive into your folder structure.")
	# Multiple argument commands
	print(f"\n--- Multiple argument commands ---")
	print(f"'cd <foldername>' to navigate inside the folder")
	print(f"'info <foldername>' to get more information on the folder.")
	print(f"'info <filename>' to get more information on the file.")

	print(f"What would you like to do: ")
	return input("Input: ")


def user_command():
	"""
	Takes strings as user input.
	Returns a list with command keywords.
	"""
	commands_list = []
	tmp_cmd = ""

	print(f"What would you like to do?")
	user_input = input("Input: ")
	for i in user_input.lower():
		if i.isalpha:
			tmp_cmd += i
		# in case of space (multiple commands)
		elif i.isspace:
			commands_list.append(tmp_cmd)
			tmp_cmd = ""

	commands_list.append(tmp_cmd)
	return commands_list


def scan_directory(path):
	# TODO: 
	""" 
	Call get_file_info() on every file found
	Return a list of all those info dicts
	"""
	folders, files = show_files_and_folders(path) # TODO: update function -> no print statement
	pass
	for f in folders:
		get_folder_info(f)
	for f in files:
		get_file_info(f)


def show_files_and_folders(path):
	"""
	Takes a directory path and prints two lists containing files and folders.
	Returns two lists of both folders and files.
	"""
	folders = [item for item in os.listdir(path)
			   if os.path.isdir(os.path.join(path, item)) and not item.startswith('.')]
	files = [item for item in os.listdir(path)
			 if os.path.isfile(os.path.join(path, item)) and not item.startswith('.')]

	print("📂 Folders:")
	for f in folders:
		print(f"  {f}", end="\t")
	print()
	print("\n📑 Files:")
	for f in files:
		print(f"  {f}", end="\t")
	print()
	
	return folders, files


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


def get_folder_info(folderpath):
	# TODO
	""" get_file_info(filepath)
	takes a filepath
	grab info with os.stat()
	return dict with all data?
	"""
	stats = os.stat(os.path.join(folderpath))	# add join
	date = datetime.fromtimestamp(stats.st_mtime)


	# folders = [item for item in os.listdir(folderpath)
	# 		   if os.path.isdir(os.path.join(path, item)) and not item.startswith('.')]
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

def organise_by_extenstion(file_list):
	# TODO: organise output by extension
	""" organise_by_extenstion(file_list)
		takes list from scan_directorty and groups files by extension
	"""
	pass

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