# 08_inherit.py

#此示例示意继承与派生

class Human:
    '''此类用来描述人类共性行为'''
    def say(self, that):
        print("说：", that)
    def walk(self, distance):
        print("走了", distance, '公里')


class Student(Human):
    #def say(self, that):
    #    print("说：", that)
    #def walk(self, distance):
    #    print("走了", distance, '公里')
    def study(self, subject):
        print('正在学习', subject)

class Teacher(Human):
    def teach(self, subject):
        print('正在教：', subject)

h1 = Human()
h1.say('今天天气真热')
h1.walk(5)

print('------------以下学生对象行为-------------')
s1 = Student()
s1.say('学习有点累')
s1.walk(3)
s1.study('python')

t1 = Teacher()
t1.say('明天星期六了')
t1.walk(6)
t1.teach('面向对象')