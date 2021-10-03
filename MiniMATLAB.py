"""
https://www.mathworks.com/help/matlab/ref/matlabwindows.html
"""


from main.script_execute import script_execute
from main.repl_execute import repl_execute
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, nargs='?', help='program read from script file')
parser.add_argument('-t', '--token', default=False, help='print tokens', action="store_true")
parser.add_argument('-a', '--ast', default=False, help='print abstract syntax tree', action="store_true")
parser.add_argument('-v', '--var', default=False, help='print variables', action="store_true")

args = parser.parse_args()

if args.file:
    script_execute(args.file, print_tokens=args.token, print_ast=args.ast, print_var=args.var)
else:
    repl_execute(print_tokens=args.token, print_ast=args.ast, print_var=args.var)
