def max_odd(array):
    res = None
    for el in array:
        if isinstance(el, (int, float)) and (res is None or el > res) and el % 2 == 1:
            res = el
    return int(res) if isinstance(res, float) else res
