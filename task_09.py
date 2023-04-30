def connect_dicts(dict1, dict2):
    def summ_of_dict_values(dictionary):
        summ = 0
        for elem in dictionary.values():
            summ += elem
        return summ

    def update_with_filter_more_than_10(high_d, low_d):
        res_d = dict()
        for key, value in low_d.items():
            if value >= 10:
                res_d[key] = value

        for key, value in high_d.items():
            if value >= 10:
                res_d[key] = value

        return res_d

    if summ_of_dict_values(dict2) >= summ_of_dict_values(dict1):
        updated_dict = update_with_filter_more_than_10(dict2, dict1)
    else:
        updated_dict = update_with_filter_more_than_10(dict1, dict2)

    return dict(sorted(updated_dict.items(), key=lambda x: x[1]))
