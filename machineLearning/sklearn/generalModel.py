from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def general_model1():
    """
    k近邻函数模型
    :return:
    """
    # 通用步骤1. 加载数据
    iris = datasets.load_iris()
    # 通用步骤2. 导入数据和标签
    iris_X = iris.data
    iris_y = iris.target
    # 通用步骤3. 划分为训练集和测试集数据
    X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.3)
    # print(y_train)
    # 通用步骤4. 添加模型，这里设置knn分类器
    knn = KNeighborsClassifier()
    # 通用步骤5. 进行训练
    knn.fit(X_train, y_train)
    # 通用步骤6. 使用训练好的knn进行数据预测
    y_predict = knn.predict(X_test)
    print(y_predict)
    # 通用步骤7. 查看报告
    print('The Accuracy of Naive Bayes Classifier is:', knn.score(X_test, y_test))
    print(classification_report(y_test, y_predict))
    # print(classification_report(y_test, y_predict, target_names=news.target_names))


def general_model2():
    # 导入数据集
    # 这里将全部数据用于训练，并没有对数据进行划分，上例中
    # 将数据划分为训练和测试数据，后面会讲到交叉验证
    loaded_data = datasets.load_boston()
    data_X = loaded_data.data
    data_y = loaded_data.target

    # 设置线性回归模块
    model = LinearRegression()
    # 训练数据，得出参数
    model.fit(data_X, data_y)

    # 利用模型，对新数据，进行预测，与原标签进行比较
    print(model.predict(data_X[:4, :]))
    print(data_y[:4])
