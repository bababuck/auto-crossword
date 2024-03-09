""" Parse crossword files recieved from generator and convert to Latex

Also interface with the clue generator.

Outputs into latex file format:
https://tex.stackexchange.com/questions/44775/how-to-create-a-crossword-
puzzle-in-latex
"""

backslash = '\\'
newLine = '\n'


class CrosswordSquare:
    """ A single square in the crossword puzzle.

    Contains information about the clue number that is associated with the
    square.
    Also needs to know the letter that will fill the square.
    """
    def __init__(self, value="*", label=None):
        self.value = value
        self.label = label

    def __str__(self):
        """ Return value and optional label into Latex format. """
        return f"{f'[{self.label}]' if self.label is not None else ''}" \
            f"{self.value}"


class CrosswordRow:
    """ A full row in a crossword puzzle.

    Needs to know how to print itself into Latex form.
    """
    def __init__(self, row_str, row_num, clue_locs):
        self.squares = []
        for col_num, square_char in enumerate(row_str.rstrip()):
            loc_str = f'{row_num},{col_num}'
            if square_char == '#':
                square_char = '*'
            self.append(CrosswordSquare(square_char, clue_locs.get(loc_str)))

    def __len__(self):
        return len(self.squares)

    def __getitem__(self, key):
        return self.squares[key]

    def append(self, square):
        """ Add an additional square to the row. """
        self.squares.append(square)

    def __str__(self):
        return "|" + "|".join(map(str, self.squares)) + "|."


class CrosswordBoard:
    def __init__(self, board_file, clue_locs={}):
        """ Parse a file for relevant board information.

        Clue labels are provided as a dictionary.
        """
        self.rows = []
        with open(board_file, "r") as board:
            for row_num, row in enumerate(board):
                self.append(CrosswordRow(row, row_num, clue_locs))

    @property
    def row_cnt(self):
        """ Return the number of rows. """
        return len(self.rows)

    @property
    def col_cnt(self):
        """ Return the number of columns, assumes a square board."""
        if self.rows:
            return len(self.rows[0])
        else:
            return 0

    def append(self, row):
        """ Append a new row to the board. """
        self.rows.append(row)

    def __str__(self):
        return f"""
        {backslash}begin{{Puzzle}}{{{self.col_cnt}}}{{{self.row_cnt}}}
        {newLine.join(map(str,self.rows))}
        {backslash}end{{Puzzle}}
        """


class CrosswordClue:
    """ A single clue in a crossword puzzle. """
    def __init__(self, number, answer, hint):
        self.number = number
        self.answer = answer
        self.hint = hint

    def __str__(self):
        return f"{backslash}Clue{{{self.number}}}" \
            f"{{{self.answer}}}{{{self.hint}}}"


class CrosswordClues:
    """ Store relevant information about all crossword clues. """
    def __init__(self, direction):
        self.direction = direction
        self.clues = []

    @property
    def dir(self):
        return self.direction[0].lower()

    def append(self, crossword_clue):
        self.clues.append(crossword_clue)

    def __str__(self):
        return f"""
        {backslash}begin{{PuzzleClues}}{{{backslash}textbf{{{self.direction}}}}}

        {(newLine * 2).join(map(str, self.clues))}

        {backslash}end{{PuzzleClues}}
        """


class SolutionLine:
    """A single line in the solution file."""
    def __init__(self, solution_line):
        info = solution_line.rstrip().split(" ")
        self.number = info[0]
        self.row = info[1]
        self.col = info[2]
        self.answer = info[3]


class PuzzleGenerator:
    """ Manages the parts of a crossword.

    Parses the required files for generating a crossword.
    """
    def __init__(self):
        clue_locs = {}
        self.clue_sets = [CrosswordClues('Across'), CrosswordClues('Down')]
        for clue_set in self.clue_sets:
            with open(f"{clue_set.dir}_words.txt", "r") as solution_file:
                for solution_line in solution_file:
                    sol_info = SolutionLine(solution_line)
                    clue_locs[f'{sol_info.row},{sol_info.col}'] = \
                        sol_info.number
                    clue_set.append(CrosswordClue(sol_info.number,
                                                  sol_info.answer,
                                                  sol_info.answer))

        self.board = CrosswordBoard("filled_grid.txt", clue_locs)

    def __str__(self):
        return f"""
        {backslash}documentclass{{article}}
        {backslash}usepackage[unboxed]{{cwpuzzle}}
        {backslash}begin{{document}}
        {self.board}
        {(newLine * 2).join(map(str, self.clue_sets))}
        {backslash}pagebreak
        {backslash}PuzzleSolution
        {self.board}
        {backslash}end{{document}}
        """


if __name__ == '__main__':
    puzzle_generator = PuzzleGenerator()
    print(puzzle_generator)
