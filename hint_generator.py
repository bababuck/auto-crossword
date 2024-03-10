""" Crossword interface with GPT-3.5.

Functionality is to ask for a clue for a certain word.
"""

from openai import OpenAI


class HintGenerator:
    """Knows how to generate a crossword hint."""
    def __init__(self):
        """Initialize OpenAI client."""
        self.client = OpenAI()

    def __call__(self, solution_word):
        """Generate a crossword hint given a clue.

        Does this via request to GPT.
        """
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "user",
                 "content":
                 f"write a cross word clue for "
                 f"{solution_word} using the fewest tokens possible."}
            ]
        )
        return response.choices[0].message.content
