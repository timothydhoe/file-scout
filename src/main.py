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
	pass
	"""
	Control input from user
	"""
	# user_input = input("blah blah")




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
	returns something? Dunno what yet --> file list
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
	stats = os.stat(filepath)
	extention = os.path.splitext(filepath)

	return {
		'path': filepath,
		'size': stats.st_size,
		'modified': datetime.fromtimestamp(stats.st_mtime),
		'ext': extention[-1],
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


def format_size():
	""" format_size
		converts output to readable
		1024 bytes = 1KB
		1024 KB = 1MB
		1024 MB = 1GB
	"""
	pass

# if __name__ == "__main__":
# 	main():



dict ={}
dict = get_file_info(r'/Users/timothydhoe/Syntra/2025_DS_VDO/Automate the Boring Stuff with Python.pdf')

for keys, values in dict.items():
	print(f"{keys}: {values}")