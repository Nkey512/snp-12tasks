def sort_list(lst):
    if len(lst) == 0:
        return lst

    max_el, min_el = lst[0], lst[0]
    max_idx_list, min_idx_list = [], []

    for idx, el in enumerate(lst):
        if el > max_el:
            max_el = el
            max_idx_list.clear()
        elif el < min_el:
            min_el = el
            min_idx_list.clear()
        if el == max_el:
            max_idx_list.append(idx)
        if el == min_el:
            min_idx_list.append(idx)

    for index in max_idx_list:
        lst[index] = min_el
    for index in min_idx_list:
        lst[index] = max_el

    lst.append(min_el)
    return lst
