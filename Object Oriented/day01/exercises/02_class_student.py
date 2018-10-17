#练习:
#  修改前的Student 类,
#   1) 为该类添加初始化方法,实现在创建对象时自动设置 '姓名', '年龄', '成绩' 属性
#   2) 添加set_score方法能为对象修改成绩信息
#   3) 添加show_info方法打印学生对象的信息

class Student:
    def __init__(self, name, age=0, score=0):
        '''初始化方法用来给学生对象添加'姓名'和'年龄'属性'''
        # 此处自己实现
        self.name = name
        self.age = age
        self.score = score

    def set_score(self, score):
        self.score = score

    def show_info(self):
        '''此处显示此学生的信息'''
        print(self.name,'今年',self.age,'岁',
              '成绩是',self.score)

s1 = Student('小张', 20, 100)
s2 = Student('小李', 18, 90)

s1.show_info()  # 小张信息
s2.show_info()  # 小李信息

s1.set_score(97)
s1.show_info()  # 成绩修改

