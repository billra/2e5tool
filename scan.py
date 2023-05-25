# scan.py
# Bill Ola Rasmussen

from argparse import ArgumentParser
from collections import defaultdict
import os

htmext='.htm','.html'

def doFile(path,file,ftc):
    ext=os.path.splitext(file)[1]
    ftc[ext if ext else 'none']+=1
    if ext.lower() not in htmext:
        print(f'skip: {file}')
        return
    print(f'do: {file}')
    # doFile(os.path.join(path, file))

def doAllFiles(root,ftc):
    for path, dirs, files in os.walk(root):
        # Skip hidden directories
        dirs[:]=[d for d in dirs if not d.startswith('.')] # note slice assignment
        for file in files:
            doFile(path,file,ftc)

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

# <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"> --> <!DOCTYPE html>
# <HTML>
# <HEAD>
# <TITLE>NPWC Falken</TITLE>
# <META NAME="author" CONTENT="Bill Ola Rasmussen">
# <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
# <meta name="keywords" content="NASA, Parawing, Research, npw, singleskin">
# <link rel="stylesheet" type="text/css" href="/style.css">
# <link rel="shortcut icon" href="/favicon.ico" type="image/vnd.microsoft.icon">
# <link rel="icon" href="/favicon.ico" type="image/vnd.microsoft.icon">
# </HEAD>
# <BODY>
# <div class="head">
# <div class="rflo">
# <a href="/"><img src="/img/2e5.jpg" width="277" height="42" alt="2e5.com" ></a></div>
# <h1>NPWC Falken</h1></div>
# <div class="navBar">
# <div class="rflo">
# tags:
# <a href="/tags/kite/">kite</a>
# </div>
# <a href="../../..">2e5</a> &raquo;
# <a href="../..">kite</a> &raquo;
# <a href="..">npwc</a> &raquo;
# Falken
# </div>
# <div class="main">
# ...
# </div>
# <div class="navBar">
# <div class="rflo">
# tags:
# <a href="/tags/kite/">kite</a>
# </div>
# <a href="../../..">2e5</a> &raquo;
# <a href="../..">kite</a> &raquo;
# <a href="..">npwc</a> &raquo;
# Falken
# </div>
# <p>
# <a href="http://validator.w3.org/check?uri=referer">
# <img src="/img/valid-html401.png" alt="Validate HTML 4.01 Strict" height="31" width="88"></a> <-- update to 5?
# <a href="http://jigsaw.w3.org/css-validator/check/referer">
# <img src="/img/valid-css.png" alt="Validate CSS" height="31" width="88"></a> <-- still the same?
# <p>&copy;2016 Bill Ola Rasmussen
# </BODY>
# </HTML>
