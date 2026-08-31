import argparse
import os


def init(args):
    print("Initialized empty Git repository")
    os.mkdir('.tinygit')
    os.mkdir('.tinygit/objects')
    os.mkdir('.tinygit/refs')
    os.mkdir('.tinygit/refs/heads')
    with open('.tinygit/HEAD', 'w') as f:
        f.write('ref: refs/heads/master\n')


# create the top-level parser
parser = argparse.ArgumentParser(
    prog='tinygit', description='A simple git prototype')
subparsers = parser.add_subparsers(help='tinygit commands')

# create the parser for the "a" command
init_parser = subparsers.add_parser(
    'init', help='initialize git repository')
init_parser.set_defaults(func=init)

# create the parser for the "b" command
hash_object_parser = subparsers.add_parser(
    'hash-object', help='hash a file and print the object name')
hash_object_parser.add_argument('file', help='file to hash')

add_parser = subparsers.add_parser(
    'add', help='add file contents to the index')
add_parser.add_argument('file', help='file to add to the index')

commit_parser = subparsers.add_parser(
    'commit', help='record changes to the repository')
commit_parser.add_argument(
    '-m', '--message', required=True, help='commit message')

args = parser.parse_args()

if hasattr(args, "func"):
    args.func(args)
else:
    parser.print_help()
