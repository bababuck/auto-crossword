""" Driver for creating a crossword puzzle.

Will take command line options to help guide puzzle generation.
"""

import argparse
import crossword_compiler
import crossword_parser

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

    args = parser.parse_args()
    if not crossword_compiler.generate_crossword(args.wordlist,
                                                 args.gridfile,
                                                 args.seedlist,
                                                 args.minscore):
        puzzle_generator = crossword_parser.PuzzleGenerator()
        print(puzzle_generator)
