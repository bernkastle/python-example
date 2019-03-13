import json

class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def work(self):
        print(self.name, 'is working...')


aa = Person('Bob', 23, 'Student')

with open('abc.json', 'w', encoding='utf-8') as f:
    # 类的序列化
    json.dump(aa, f, default=lambda obj: obj.__dict__)
