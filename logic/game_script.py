import argparse
import chess_engine as ce
import os

def create(nargs) -> None:
    ce.create_board(nargs.name)


def turn(nargs) -> None:
    ce.write_turn(nargs.initial, nargs.final, nargs.name, nargs.color)

def delete_file(nargs) -> None:
    if os.path.isfile(nargs.name):
        os.remove(nargs.name)


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

parser_create = subparsers.add_parser('create')
parser_create.add_argument('name', type=str)
parser_create.set_defaults(func=create)

parser_turn = subparsers.add_parser('turn')
parser_turn.add_argument('initial', type=str)
parser_turn.add_argument('final', type=str)
parser_turn.add_argument('name', type=str)
parser_turn.add_argument('color', type=str)
parser_turn.set_defaults(func=turn)

parser_create = subparsers.add_parser('delete')
parser_create.add_argument('name', type=str)
parser_create.set_defaults(func=delete_file)

# args = parser.parse_args('create abiba'.split())
# args = parser.parse_args('turn a2 a3 abiba w'.split())
# args = parser.parse_args('delete abiba'.split())
args = parser.parse_args()
args.func(args)
