"""
https://www.mathworks.com/help/matlab/ref/matlabwindows.html
"""


from main.script_execute import script_execute
from main.repl_execute import repl_execute
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, nargs='?', help='program read from script file')
parser.add_argument('-t', '--t', type=bool, default=False, help='print tokens')
parser.add_argument('-a', '--a', type=bool, default=False, help='print abstract syntax tree')
parser.add_argument('-v', '--v', type=bool, default=False, help='print variables')

args = parser.parse_args()

if args.file:
    script_execute(args.file, print_tokens=args.t, print_ast=args.a, print_var=args.v)
else:
    repl_execute(print_tokens=args.t, print_ast=args.a, print_var=args.v)
