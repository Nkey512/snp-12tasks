import string
from collections import Counter


def count_words(seq):
    word_list = seq.translate(seq.maketrans('', '', string.punctuation)).lower().split()
    c = Counter(word_list)
    return dict(c)


def count_words_no_counter(seq):
    word_list = seq.translate(seq.maketrans('', '', string.punctuation)).lower().split()
    d = dict()
    for el in word_list:
        d[el] = d.get(el, 0) + 1
    return d
