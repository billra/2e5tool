# scan.py
# Bill Ola Rasmussen

from argparse import ArgumentParser
import os

def doFile(file):
    print(f'do: {file}')

def doAllFiles(root):
    for path, dirs, files in os.walk(root):
        # Skip hidden directories
        dirs[:]=[d for d in dirs if not d.startswith('.')] # note slice assignment
        for file in files:
            doFile(os.path.join(path, file))

def main():
    print('scan')
    parser = ArgumentParser()
    parser.add_argument('-r', '--root', default='.', help='root of site to scan, defaults to cwd')
    args=parser.parse_args()
    root=os.path.abspath(args.root)
    print(f'parsing site at: {root}')
    doAllFiles(root)
    print('done.')

if __name__ == '__main__':
    main()
