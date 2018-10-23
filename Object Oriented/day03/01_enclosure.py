#01_enclosure.py

#此示例示意使用私有属性和私有方法：
class A:
    def __init__(self):
        self.__p1 = 100 #p1为私有属性

    def test(self):
        print(self.__p1)

    def __m1(self):
        print("我是A类的__m1方法！")

a = A()
print(a.__p1)     #在类外看不到__p1属性，访问失败！
 
a.test()          #类内方法test调用私有属性

a.__m1()          #出错，无法调用私有方法