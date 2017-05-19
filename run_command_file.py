'''
A sample program to execute commands for specific files in a directory.
The directory structure is walked in recursive fashion
'''

import os
import sys
import fnmatch
from subprocess import call

cwd = os.getcwd().split(os.sep)[-1]
if (cwd != 'foo'):
    print "Error: Run this script from foo directory"
    exit()

blah_dir = os.getcwd() + os.sep + "bar/blah"
for dir_path, dirnames, files in os.walk(blah_dir):
    for file in  fnmatch.filter(files, 'foo.txt'):
        full_file_path = os.path.join(dir_path, file)
        call(["ls", full_file_path)
