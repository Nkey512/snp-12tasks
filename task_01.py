import string


def is_palindrome(seq):
    seq = str(seq).lower()
    pure_seq = seq.translate(seq.maketrans('', '', string.punctuation + ' '))
    i = 0
    j = len(pure_seq) - 1
    while i < j:
        if pure_seq[i] != pure_seq[j]:
            return False
        i += 1
        j -= 1
    return True
