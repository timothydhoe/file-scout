"""
FILE SCOUT
----------
file: main.py

Programme that helps users become more intimate with their files and folders.

"""

import os
from datetime import datetime

path = ""

def main():
	dict ={}
	dict = get_file_info(r'<FILEPATH>')

	for keys, values in dict.items():
		print(f"{keys}: {values}")
	"""
	Control input from user
	user_input = input("Give me a path: ")
	if os.path.exists(<path-to-file>):
	"""
	# 
	# Or get current working dir? os.getcwd?

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




def files_by_type(filepath):
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

def scan_directory(path):
	""" 
	Takes a path
	Returns something? Dunno what yet --> file list
"""
	pass

def get_folder_info(folderpath):
	""" get_file_info(filepath)
	takes a filepath
	grab info with os.stat()
	return dict with all data?
	"""
	folders = {}
	files = {}
	for item in folderpath:
		if item.is_dir:
			pass
			# recursive shit happening here
		if item.is_file:
			# Store
			pass



def get_file_info(filepath):
	"""
	Take the path of a file and outputs size, last modified and the extension.
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


# test = os.stat('/Users/timothydhoe/Syntra')
# print(test)

# readable_date = datetime.fromtimestamp(test.st_mtime)
# print(readable_date)

# readable_size = test.st_size
# print(f"{readable_size} bytes")

# readable_uid = test.st_mode
# print(readable_uid)


def organise_by_extenstion(file_list):
	""" organise_by_extenstion(file_list)
		takes list from scan_directorty and groups files by extension
	"""
	pass


def format_size(size_in_bytes):
	"""
	Transforms general output in bytes into readable sizes.
	Returns size in KB, MB or GB
	"""
	if size_in_bytes >= (1_024 ** 3):
		return f"{size_in_bytes / (1_024 ** 3):.2f} GB"
	elif size_in_bytes > (1_024 ** 2):
		return f"{size_in_bytes / (1_024 ** 2):.2f} MB"
	elif size_in_bytes > 1_024:
		return f"{size_in_bytes / 1_024:.2f} KB"
	else:
		return f"{size_in_bytes} bytes"

if __name__ == "__main__":
	main()