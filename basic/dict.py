def get_max_value_from_dict():
    """
    从字典中取出最大值
    :return:
    """
    p = {'a': 1, 'b': 2, 'c': 4, 'd': 3}
    return max(p, key=p.get)
