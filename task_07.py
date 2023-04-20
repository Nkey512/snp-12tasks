def combine_anagrams(words_array):
    d = dict()

    for word in words_array:
        d.setdefault(str(sorted(word)), []).append(word)

    res = []
    for value in d.values():
        res.append(value)

    return res
