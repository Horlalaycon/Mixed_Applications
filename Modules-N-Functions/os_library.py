"""
os library is a built-in python library that provides functions for interacting with the operating system.
please note: specify the path if it is an absolute path.
"""
# importing the os library
import os


#           File system operations include:
# creating files and directory
os.mkdir("directory_name")

# removing directory
os.rmdir("directory_name")
# removing files
os.remove("filename")

# renaming files and directory
os.rename("old_dir", "new_dir")

# listing directory contents
os.listdir("path")

# checking file existence and attributes
os.path.exists("path")

# getting file size and modification time
os.path.getsize("filename")
os.path.getmtime("filename")

# changing file permissions
