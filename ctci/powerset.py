def power_set(big_set, res):
    if len(big_set) == 0:
        return res
    elif len(big_set) == 1:
        res.append(set[0])
    else:
        res = power_set(big_set)