from operator import itemgetter
from collections import Counter


def get_max_from_tuple_list():
    """
    Python tuple list 按照值取最大
    :return: value最大的tuple
    """
    data = [('a', 10), ('b', 20), ('c', 15)]
    data_max = max(data, key=itemgetter(1))
    return data_max


def count_value():
    """
    对python list的值进行计数
    :return: 每个元素出现次数，字典类型
    """
    data = [1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    counter = Counter(data)
    return counter
