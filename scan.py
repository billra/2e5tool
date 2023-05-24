# scan.py
# Bill Ola Rasmussen

from argparse import ArgumentParser
from collections import defaultdict
import os

def doFile(file):
    print(f'do: {file}')

def doAllFiles(root,ftc):
    for path, dirs, files in os.walk(root):
        # Skip hidden directories
        dirs[:]=[d for d in dirs if not d.startswith('.')] # note slice assignment
        for file in files:
            ext=os.path.splitext(file)[1]
            ftc[ext if ext else 'none']+=1
            doFile(os.path.join(path, file))

def main():
    print('scan')
    parser = ArgumentParser()
    parser.add_argument('-r', '--root', default='.', help='root of site to scan, defaults to cwd')
    args=parser.parse_args()
    root=os.path.abspath(args.root)
    print(f'parsing site at: {root}')
    ftc=defaultdict(int) # file type count
    doAllFiles(root,ftc)
    print('files:')
    for key,val in sorted(ftc.items()):
        print(f'  {key}: {val}')
    print('done.')

if __name__ == '__main__':
    main()
