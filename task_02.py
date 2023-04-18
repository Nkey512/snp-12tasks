def coincidence(lst=None, rang=None):
    if lst is None or rang is None:
        return []
    return list(filter(lambda x: type(x) in (int, float) and rang.start <= x < rang.stop, lst))
