""" Crossword interface with GPT-3.5.

Functionality is to ask for a clue for a certain word.
"""


class HintGenerator:
    """Knows how to generate a crossword hint."""
    def __init__(self):
        pass

    def __call__(self, solution_word):
        """Generate a crossword hint given a clue."""
        return solution_word
