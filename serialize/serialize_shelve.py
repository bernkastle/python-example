import shelve

"""
shelve模块可以看做是pickle模块的升级版，因为shelve使用的就是pickle的序列化协议，但是shelve比pickle提供的操作方式更加简单、方便。shelve模块相对于其它两个模块在将Python数据持久化到本地磁盘时有一个很明显的优点就是，它允许我们可以像操作dict一样操作被序列化的数据，而不必一次性的保存或读取所有数据。
"""

# 自定义class
class Student(object):
    def __init__(self, name, age, sno):
        self.name = name
        self.age = age
        self.sno = sno

    def __repr__(self):
        return 'Student [name: %s, age: %d, sno: %d]' % (self.name, self.age, self.sno)


# 保存数据
tom = Student('Tom', 19, 1)
jerry = Student('Jerry', 17, 2)

with shelve.open("stu.db") as db:
    db['Tom'] = tom
    db['Jerry'] = jerry

# 读取数据
with shelve.open("stu.db") as db:
    print(db['Tom'])
    print(db['Jerry'])
