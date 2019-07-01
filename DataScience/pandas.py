import pandas as pd
from sklearn.preprocessing import LabelEncoder


def filter_phone_number():
    """
    使用正则表达式过滤电话号码
    :return: pandas Dataframe
    """
    data = pd.read_excel('data.xlsx')

    # 数据清洗，移除多余字符
    data.contacttel = data.contacttel.str.replace('-', '').replace(' ', '')

    # 使用正则表达式过滤无效的电话号码，na=False的意思时过滤缺失值
    data = data[data.contacttel.str.contains(r'(^[8,6]\d{7}$)|(^0[1-9]\d{1,2}\\d{7,8}$)|(^1[3456789]\d{9}$)',
                                             na=False,
                                             regex=True)]
    return data


def data_encode():
    """
    对pandas数据进行编码，使用sklearn
    :return:
    """
    # 使用sklearn的编码器，sklearn还有binary编码器，进行onehot编码
    # pandas自身可以使用factorize进行编码，但是需要自行转化为dataframe
    lb_make = LabelEncoder()

    data = pd.read_excel('test.xlsx')
    data["encode"] = lb_make.fit_transform(data["contacttel"])

    return data


def groupby_filter():
    """
    对groupby后的pandas dataframe进行过滤
    :return:
    """
    data = pd.read_excel('门店归一.xlsx')

    # 对count > 1的数据进行过滤
    data = data.groupby('col1').filter(lambda x: len(x) > 1)
    return data


def sort_multiindex_by_index_and_column(data: pd.DataFrame) -> pd.DataFrame:
    """
    多重索引对index和column同时进行排序
    :param data: 原始数据集
    :return: 排序后的数据集
    """
    df = data.groupby(['category', 'baseunitname'])\
        .agg({'ean_basebarcode': 'count'})\
        .sort_values(by=['category', 'ean_basebarcode'], ascending=[0, 0])  # 使用排序时，分别传入index和column name，后面的ascending也需要传入数组
    return df
