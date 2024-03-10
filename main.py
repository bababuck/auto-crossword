""" Driver for creating a crossword puzzle.

Will take command line options to help guide puzzle generation.
"""

import argparse
import crossword_compiler
import crossword_parser


class IllegalArgumentError(Exception):
    """An illegal combination of command line arguments were specified."""


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a crossword puzzle')
    parser.add_argument('--wordlist',
                        help='wordlist for filing the puzzle',
                        default='project-3-crossword-compiler-bababuck/'
                        'wordlists/spreadthewordlist.txt')
    parser.add_argument('--gridfile',
                        help='grid to use for the puzzle',
                        default='project-3-crossword-compiler-bababuck/'
                        'grids/5x5blankgrid.txt')
    parser.add_argument('--seedlist',
                        help='seeds for the puzzle, '
                        'will preferentially insert',
                        default='')
    parser.add_argument('--minscore',
                        help='Minimum word score to accept',
                        type=int,
                        default=50)
    parser.add_argument('--queryword',
                        help='Word to preferentially choose words related too',
                        default="")
    parser.add_argument('--seedword-modifier',
                        help='Append this to seed words to '
                        'help guide clue generation',
                        default='')
    parser.add_argument('--difficulty',
                        help='How hard to make crossword clues',
                        default='easy')

    args = parser.parse_args()

    if args.seedlist == "" and args.seedword_modifier != "":
        raise IllegalArgumentError(
            "Cannot have seedword-modifier without a seedlist")

    if not crossword_compiler.generate_crossword(args.wordlist,
                                                 args.gridfile,
                                                 args.seedlist,
                                                 args.minscore,
                                                 args.queryword):
        puzzle_generator = crossword_parser.PuzzleGenerator(
            args.seedword_modifier, args.seedlist, args.difficulty)
        print(puzzle_generator)
