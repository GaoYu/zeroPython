#05_mro.py

#多继承中super()是按照__mro__的顺序进行基类排序的

class A:
    def m(self):
        print("A.m")

class B(A):
    def m(self):
        print("B.m")
        super().m()

class C(A):
    def m(self):
        print("C.m")
        super().m()


class D(B, C):
    '''D类继承自B,C'''
    def m(self):
        print("D.M")
        super().m()

d = D()
d.m()

for x in D.__mro__:
    print(x)
