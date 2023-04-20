def multiply_numbers(variable=None):
    if not variable:
        return

    s = str(variable)
    mult = 1
    digit_contained = False
    for ch in s:
        if ch.isdigit():
            mult *= int(ch)
            digit_contained = True

    if digit_contained:
        return mult
    return
