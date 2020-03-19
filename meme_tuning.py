# Main Method that takes in user input and output meme tunings
# Compares to see if word exists in the english directory
# Use multithreading to improve in large test cases

import all_available_tuning
import concurrent.futures
import time
import random

__string_num = int(input('Enter the number of strings on your instrument: '))
__list_of_notes = ['a','b','c','d','e','f','g','m','s']

# Gets all available meme tuning for a 6 string instrument from a 12-tone equal temperament scale
a = all_available_tuning.AllAvailableTuning(__list_of_notes, __string_num)
unfiltered_names = a.get_letter_combos()

# Implementing multi-processing to improve performance
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(a.add_validate_words, unfiltered_name) for unfiltered_name in unfiltered_names]
    
    for f in concurrent.futures.as_completed(results):
        f.result()

t2 = time.perf_counter()
available_tuning = a.get_list_of_words()

print(f'Execution time is: {t2} seconds')
print(f'The available tuning are \n {available_tuning}')
print(f'Randomly selected tuning for the {__string_num} stringed instrument is: \n \t{available_tuning[random.randrange(0, len(available_tuning) + 1, 2)]}')