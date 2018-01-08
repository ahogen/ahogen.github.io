#!/sr/env python3
"""
Author:  Alex Hogen <https://github.com/ahogen>
Created: 2018-01-07

This script looks for HTML, CSS, and JavaScript files in the provided directory
and minify's them, removing whitespace and comments, and then compresses them,
using gzip.
"""

import os
import sys
import gzip
import argparse
from htmlmin import minify as minhtml
from csscompressor import compress as mincss
#from slimit import minify as minjs
from jsmin import jsmin as minjs

def cmdline_args():
    # Make parser object
    p = argparse.ArgumentParser(description=
        """
        This is a test of the command line argument parser in Python.
        """,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    p.add_argument("start_path",
                   help="Root directory path to start looking for files to minify & compress")
    # p.add_argument("required_int", type=int,
    #                help="req number")
    # p.add_argument("--on", action="store_true",
    #                help="include to enable")
    # p.add_argument("-v", "--verbosity", type=int, choices=[0,1,2], default=0,
    #                help="increase output verbosity")
                   
    # group1 = p.add_mutually_exclusive_group(required=True)
    # group1.add_argument('--enable',action="store_true")
    # group1.add_argument('--disable',action="store_false")

    return(p.parse_args())

def minify_and_compress_each(path):

    path = str(path)

    for root, dirs, files in os.walk(path):
        
        for f in files:
            fname, fext = os.path.splitext(f)
            fext = fext.lower()

            s = ''
            was_minified = False
            should_zip = False

            if fext in '.html .css .js .xml .svg':
                should_zip = True
                fpath = os.path.join(root, f)
                s = read_file_to_string(fpath)

            if fext == '.html' or fext == '.xml':
                s = minhtml(s)
                was_minified = True
                print("HTMLmin:", fpath)
            elif fext == '.css':
                s = mincss(s)
                was_minified = True
                print("CSScompressor:", fpath)
            elif fext == '.js':
                #continue
                s = minjs(s)
                was_minified = True
                print("JSmin:", f)

            # Compress (if needed) before writing back
            if was_minified or should_zip:
                os.remove(fpath)

                if should_zip:
                    s = s.encode(encoding='utf_8')
                    with gzip.open(fpath + '.gz', 'w') as gzf:
                        gzf.write(s)
                else:
                    # Simply overwrite the original file with the
                    # minified verison.
                    write_string_to_file(fpath, s)

def read_file_to_string(file_path):
    str = ''
    with open(file_path, mode='r') as f:
        str = f.read()
    return(str)

def write_string_to_file(file_path, str):
    with open(file_path, mode='w') as f:
        f.write(str)

if __name__ == '__main__':

    if sys.version_info<(3,0,0):
        sys.stderr.write("You need python 3.0 or later to run this script\n")
        sys.exit(1)

    args = cmdline_args()

    minify_and_compress_each(args.start_path)