#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 15/03/2019 14:12
# @Author : karl wang
# @Email: karl.wang.1991@gmail.com

from sklearn.datasets import fetch_20newsgroups  # 从sklearn.datasets里导入新闻数据抓取器 fetch_20newsgroups
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
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


def auto_search_parameter():
    """
    超参数自动搜索示例
    :return:
    """

    # 载入数据集
    iris = datasets.load_iris()
    # 设置参数遍历集合
    parameters = {'kernel': ('linear', 'rbf'), 'C': [1, 2, 4], 'gamma': [0.125, 0.25, 0.5, 1, 2, 4]}

    # 设置模型
    svr = svm.SVC()
    # 使用网格搜索方法，寻找最佳超参数
    clf = GridSearchCV(svr, parameters, n_jobs=-1)
    clf.fit(iris.data, iris.target)

    # 获取超参数搜索结果
    cv_result = pd.DataFrame.from_dict(clf.cv_results_)
    with open('cv_result.csv', 'w') as f:
        cv_result.to_csv(f)

    print('The parameters of the best model are: ')
    print(clf.best_params_)

    y_pred = clf.predict(iris.data)
    print(classification_report(y_true=iris.target, y_pred=y_pred))
