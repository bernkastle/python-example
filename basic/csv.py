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


def write_csv():
    rows = [('name1', 'karl'), ('name2', 'wang')]
    # newline解决写入文件有空行的问题，encoding解决csv打开文件乱码问题
    with open('预测.csv', 'w', encoding='utf_8_sig', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(rows)
