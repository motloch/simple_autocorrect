import pandas as pd
import numpy as np
import textdistance
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

word_freq_cnt = Counter(words)
print('Most common words:')
for w, c in word_freq_cnt.most_common()[:5]:
    print(f'{w:6} {c:>5}')
