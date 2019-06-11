from operator import itemgetter


def get_max_from_tuple_list():
    """
    Python tuple list 按照值取最大
    :return: value最大的tuple
    """
    data = [('a', 10), ('b', 20), ('c', 15)]
    data_max = max(data, key=itemgetter(1))
    return data_max
