"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html
print('\n***********\n')

# Print out the command line arguments in sys.argv, one per line:
print('sys.args:')
for arg in sys.argv:
    print(arg)

print('\n***********\n')

# Print out the OS platform you're using:
print('platform:', sys.platform)

print('\n***********\n')

# Print out the version of Python you're using:
print('python version:', sys.version)

print('\n***********\n')

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print('current process id:', os.getpid())

print('\n***********\n')

# Print the current working directory (cwd):
print('current working directory:', os.getcwd())

print('\n***********\n')

# Print out your machine's login name
print('login name:', os.getlogin())

print('\n***********\n')
