from sklearn.datasets import fetch_20newsgroups  # 从sklearn.datasets里导入新闻数据抓取器 fetch_20newsgroups
from sklearn.model_selection import train_test_split
"""
skLearn包的一些基本操作
"""


def split_train_and_test_data():
    """
    数据集分割示例，同时分割训练数据集以及标签数据
    :return:
    """
    # 1.数据获取
    news = fetch_20newsgroups(subset='all')
    print(len(news.data))  # 输出数据的条数：18846

    # 2.数据预处理：训练集和测试集分割，文本特征向量化
    x_train, x_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.25,
                                                        random_state=33)  # 随机采样25%的数据样本作为测试集
