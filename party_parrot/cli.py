"""

    Command Line Interface
    ~~~~~~~~~~~~~~~~~~~~~~

"""
import sys
import argparse
from pprint import pprint
from party_parrot import _pl


def main():
    parser = argparse.ArgumentParser(description='party_parrot')
    parser.add_argument('string', type=str, help='String to convert.')
    parser.add_argument('--dir', type=str, default='auto',
                        help="Direction. One of: 'to', 'from', 'auto'."
                             "Defaults to 'auto' [detection].")
    parser.add_argument('--copy', type=bool, default=None,
                        help='If True, copy output to clipboard')
    parser.add_argument('--key', type=int, default=1,
                        help='Key to use. Defaults to 1.')
    args = parser.parse_args()

    if args.dir == 'to':
        direction = 'forward'
    elif args.dir == 'from':
        direction = 'reverse'
    elif args.dir == 'auto':
        parrots_dict = _pl._dicts.get(tuple(_pl._dicts.keys())[0])
        # Use a generator to try and avoid the worse running time.
        if any((p in args.string for p in parrots_dict.values())):
            direction == 'reverse'
        else:
            direction == 'forward'
    else:
        raise ValueError("--dir must be one of:"
                         "'to', 'from', 'auto'.")

    if args.copy is None:
        if direction == 'forward':
            copy = True
        else:
            copy = False
    else:
        copy = args.copy

    output = _pl._mapper(string=args.string, direction=direction,
                         key=args.key, copy=copy)

    # Display Output
    pprint(output)

    sys.exit()
