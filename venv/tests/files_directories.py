'''
This is to demonstrate the usage of files & directories
'''

from pathlib import Path

path = Path()

if path.exists():
    print(path.absolute())
    for file in path.glob('*.py'):
        print(file)

