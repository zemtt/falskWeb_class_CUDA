#coding:utf-8

import pickle

class classData:
    def __init__(self):
        self.data = []
    
    def add_class(self, school, class_, date):
        if [school, class_, date] in self.data:
            return
        self.data.append([school, class_, date])
    
    def del_class(self, school, class_, date):
        self.data.remove([school, class_, date])
    
    def change(self, new_data, old_data):
        self.del_class(old_data[0], old_data[1], old_data[2])
        self.add_class(new_data[0], new_data[1], new_data[2])
    
    def search(self, school, class_):
        results = []
        for clas in self.data:
            sym = 0
            if school and school != clas[0]:
                sym = 1
            if class_ and class_ != clas[1]:
                sym = 1
            if not sym:
                results.append(clas)
        return results

def load():
    with open('./data','rb') as f:
        data = pickle.load(f)
    return data

def save(obj):
    with open('./data','wb') as f:
        pickle.dump(obj, f)
    
def add_class(school, class_, date):
    data = load()
    data.add_class(school, class_, date)
    save(data)

def del_class(school, class_, date):
    data = load()
    data.del_class(school, class_, date)
    save(data)

def change(school, class_, date, n_school, n_class_, n_date):
    data = load()
    data.change([n_school, n_class_, n_date], [school, class_, date])
    save(data)

def search_class(school='', class_=''):
    data = load()
    return data.search(school, class_)
    
def new_data():
    with open('./data','wb') as f:
        pickle.dump(classData(), f)
    add_class(u'北京林业大学',u'数据结构',u'2018/06/24')
    add_class(u'北京林业大学',u'C程序设计',u'2018/06/30')
    add_class(u'北京林业大学',u'Java实践开发',u'2018/07/12')
    add_class(u'清华大学',u'数学分析',u'2018/07/16')
    add_class(u'北京大学',u'高等代数',u'2018/07/25')
    add_class(u'哈弗大学',u'数学分析',u'2018/08/24')