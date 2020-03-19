# Helper class to output the available English Words from the available letters
# Compares to see if word exists in the english directory

# Info about each of the libraries can be found here
# PyEnchant: Spellcheck python library
#    * DOC: https://pypi.org/project/pyenchant/ 
# itertools Product: Creates Cartesian product of input iterables 
#    * DOC: https://docs.python.org/3/library/itertools.html#itertools.product

import enchant
import os
from itertools import product

class AllAvailableTuning():

    __dict = enchant.Dict("en_US")
    __list_of_words = []

    def __init__(self, arr, string_count):
        self.__arr = arr
        self.__string_count = string_count

    def add_validate_words(self, new_word):
        if(self.__dict.check(new_word)):
            self.__list_of_words.append(new_word)

    def get_letter_combos(self):
        return list(map("".join, product(self.__arr, repeat=self.__string_count)))

    def get_list_of_words(self):
        return self.__list_of_words if self.__list_of_words is not None else 'No meme tunings could be found'

