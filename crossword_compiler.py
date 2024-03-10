""" Module for interfacing with the Cpp crossword compiler.

Allows us to invoke the compiler from Python.
"""

import ctypes

crossword_compiler = ctypes.CDLL(
    'project-3-crossword-compiler-bababuck/xword.so')
crossword_compiler.generate.argtypes = (ctypes.c_char_p,
                                        ctypes.c_char_p,
                                        ctypes.c_char_p,
                                        ctypes.c_int,
                                        ctypes.c_char_p)
# Returns 0 on success, otherwise failure
crossword_compiler.generate.restype = ctypes.c_int


def generate_crossword(wordlist_path,
                       gridfile_path,
                       seedlist_path,
                       minimum_score,
                       query_word):
    wordlist_path = wordlist_path.encode('utf-8')
    gridfile_path = gridfile_path.encode('utf-8')
    seedlist_path = seedlist_path.encode('utf-8')
    query_word = query_word.encode('utf-8')
    return crossword_compiler.generate(wordlist_path,
                                       gridfile_path,
                                       seedlist_path,
                                       minimum_score,
                                       query_word)
