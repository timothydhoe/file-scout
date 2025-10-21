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

	user_dir = start_directory(cwd)
	
	while True:
		instruct = user_instructions()
		match instruct.lower():
			case 'a':
				#TODO: add and write function
				pass
			case 'i':
				show_folders(user_dir)
				foldername = input("which folder?")
				get_folder_info(user_dir)
				# TODO: write and add function (like file_info)
			case 'i -f':
				show_files(user_dir)
				filename = input("what file? ")
				# TODO: raise warning/error when file not present
				file_info = get_file_info(os.path.join(user_dir, filename))
				print_dict(file_info)
			case 's':
				print()
				show_files(user_dir)
			case 'help':
				print(f"\nI don't know where I am or what my purpose in life is, but at least I have you...\n")
			case q:
				print(f"Bye bye... 👋\n")
				break



#
# Functions
#
def start_directory(cwd):
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
	return cwd


def user_instructions():
	# TODO: add instructions for user
	print(f"1. Type 'A' to analyse.")
	print(f"2. Type 'S' to show files and folders.")
	print(f"3. Type 'I' to reveal folder information.")
	print(f"4. Type 'I -f' to reveal file information.")
	# TODO: add change directory
	# TODO: add scan directory (use os.walk())
	print(f"5. Type 'help' if you feel really lost.")
	print(f"6. Type 'q' to quit the programme.")

	return input("Input: ")


def scan_directory(path):
	# TODO: 
	""" 
	Call get_file_info() on every file found
	Return a list of all those info dicts
	"""
	pass


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
		print(f"  {f}")
	print("\n📑 Files:")
	for f in files:
		print(f"  {f}")
	print("")
	
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
	
	return folders, files


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
	pass


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