import pandas as pd
import numpy as np
from textdistance import Jaccard
import re
from collections import Counter

words = []

# Get a set of all words
with open('moby_dick.txt', 'r') as f:
    data = f.read()
    data = data.lower()
    words = re.findall('\w+', data)

V = set(words)

print(f'Moby Dick includes {len(V)} unique words')

# Count frequency of each word
word_freq_cnt = Counter(words)
print('Most common words:')
for w, c in word_freq_cnt.most_common()[:5]:
    print(f'{w:6} {c:>5}')

total_words = sum(word_freq_cnt.values())

# Relative word frequency of each word
probs = {}
for k in word_freq_cnt.keys():
    probs[k] = word_freq_cnt[k]/total_words

def my_autocorrect(input_word: str) -> pd.core.frame.DataFrame:
    """
    Print that the word is correct or return a dataframe with closest matches.

    Uses Jaccard distance to compare words and finds the most similar words to the input.

    Args:
        input_word: The word we want to correct.

    Returns:
        Either a string "Your word seems to be correct." or a dataframe with the closest
        matches, their relative frequency in the main corpus and the similarity to the
        input_word.
    """
    input_word = input_word.lower()

    if input_word in V:
        return('Your word seems to be correct.')
    else:
        similarities = [1 - Jaccard(qval=2).distance(v, input_word) for v in word_freq_cnt.keys()]
        df = pd.DataFrame.from_dict(probs, orient = 'index').reset_index()
        df = df.rename(columns={'index':'Word', 0:'Prob'})
        df['Similarity'] = similarities
        out = df.sort_values(['Similarity', 'Prob'], ascending = False).head()
        return(out)

print('\nAutocorrect  neverteless:')
print(my_autocorrect('neverteless'))

print('\nAutocorrect nesseccary:')
print(my_autocorrect('nesseccary'))

print('\nAutocorrect occurence:')
print(my_autocorrect('occurence'))

print('\nAutocorrect white:')
print(my_autocorrect('white'))
