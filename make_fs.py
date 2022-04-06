import os
import sys

def print_file(path, indent):
    if os.path.isdir(path):
        print_dir(path, indent)
    elif os.access(path, os.X_OK):
        print(f'executable(fetch("{path}"))', end='')
    else:
        print(f'file(fetch("{path}"))', end='')

def print_dir(path, indent):
    print('dir({')
    sub_indent = indent + 4
    for f in os.listdir(path):
        print(' '*sub_indent + f'"{f}":',end='')
        print_file(path + '/' + f, sub_indent)
        print(',')
    print(' '*indent + '})',end='')


path = sys.argv[1]
print('let utils = import("util.at")')
print('let dir = utils.dir')
print('let file = utils.file')
print('pub let fs = ', end='')
print_file(path, 0)
