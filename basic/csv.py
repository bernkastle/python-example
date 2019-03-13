import csv


def load_csv():
    """
    加载csv文件, 设置编码格式, 并移除第一行
    :return:
    """
    with open("fileName.csv", 'r', encoding='utf8') as f:
        csv_reader = csv.reader(f)

        # 移除第一行
        next(csv_reader)
        for row in csv_reader:
            print(row)
