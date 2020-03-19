# Takes in an input of Range of letters
# Compares to see if word exists in the english directory

# Info about each of the libraries can be found here
# PyEnchant: Spellcheck python library
#    * DOC: https://pypi.org/project/pyenchant/ 
# itertools Product: Creates Cartesian product of input iterables 
#    * DOC: https://docs.python.org/3/library/itertools.html#itertools.product

import enchant
from itertools import product

class AllAvailableTunning():
    def __init__(self, arr):
        self.arr = arr

    def find_tuning(self):
        d = enchant.Dict("en_US")
        list_of_words = []
        for n in (range(3, len(self.arr) + 1)):
            combos = list(map("".join, product(self.arr, repeat=n)))
            for combo in combos:
                if(d.check(combo)):
                    list_of_words.append(combo)
        return list_of_words


a = AllAvailableTunning(['a','b','c','d','e','f','g'])
print(a.find_tuning())