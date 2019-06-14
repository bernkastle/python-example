def get_all_max_value_from_dict():
    """
    从字典中取出所有最大值,
    :return:
    """
    p = {'a': 1, 'b': 2, 'c': 4, 'd': 3}
    max_value = max(p, key=p.get)
    # 或者使用 max_value = max(p.values)

    max_key = [k for k in p if p[k] == max_value]
    return max_key
