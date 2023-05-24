from argparse import ArgumentParser
import os

def main():
    print('scan')
    parser = ArgumentParser()
    parser.add_argument('-d', '--directory', default='.', help='directory to scan')
    args=parser.parse_args()
    path=os.path.abspath(args.directory)
    print(f'parsing site at: {path}')

    print('done.')

if __name__ == '__main__':
    main()
