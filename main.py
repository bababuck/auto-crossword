""" Driver for creating a crossword puzzle.

Will take command line options to help guide puzzle generation.
"""

import crossword_compiler
import crossword_parser

if __name__ == '__main__':
    if not crossword_compiler.generate_crossword():
        puzzle_generator = crossword_parser.PuzzleGenerator()
        print(puzzle_generator)
