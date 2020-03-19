# Takes in an input of Range of letters
# Compares to see if word exists in the english directory

# Info about each of the libraries can be found here
# PyEnchant: Spellcheck python library
#    * DOC: https://pypi.org/project/pyenchant/ 
# itertools Product: Creates Cartesian product of input iterables 
#    * DOC: https://docs.python.org/3/library/itertools.html#itertools.product

import enchant
import random
import os
import time
import concurrent.futures
from itertools import product

class AllAvailableTunning():

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
        return self.__list_of_words

# User Configurable Variables
string_num = 6
list_of_notes = ['a','b','c','d','e','f','g','m','s']

# Gets all available meme tuning for a 6 string instrument from a 12-tone equal temperament scale
a = AllAvailableTunning(list_of_notes, string_num)
unfiltered_names = a.get_letter_combos()

# Implementing multi-processing to improve performance
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(a.add_validate_words, unfiltered_name) for unfiltered_name in unfiltered_names]
    
    for f in concurrent.futures.as_completed(results):
        f.result()

t2 = time.perf_counter()
available_tuning = a.get_list_of_words()

# Output
print(f'Execution time is: {t2} seconds')
print(f'The available tuning are \n {available_tuning}')
print(f'Randomly selected tuning for the {string_num} stringed instrument is: \n \t{available_tuning[random.randrange(0, len(available_tuning) + 1, 2)]}')
