#05_mro.py

#此示例示意多继承中的方法查找顺序问题

class A:
    def m(self):
        print("A.m")

class B(A):
    def m(self):
        print("B.m")

class C(A):
    def m(self):
        print("C.m")


class D(B, C):
    '''继承自B,C'''
    def m(self):
        print("D.M")

d = D()
d.m()             #调用方法的顺序是什么？
#print(D.__mro__)  #__mro__查找顺序继承执行顺序
for x in D.__mro__:
    print(x)


