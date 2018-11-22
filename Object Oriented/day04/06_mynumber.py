#06_mynumber.py

class MyNumber:
    def __init__(self, v):
        self.data = v

    def __repr__(self):
        return 'MyNumber(%d)' % self.data

    #def myadd(self, other):
    #    v = self.data + other.data
    #    return MyNumber(v)

    def __add__(self, other):
        v = self.data + other.data
        return MyNumber(v)

    def __sub__(self, rhs):
        v = self.data - rhs.data
        return MyNumber(v)

n1 = MyNumber(100)
n2 = MyNumber(200)
#n3 = n1.myadd(n2)  #这样可以吗？

#n3 = n1.__add__(n2)

n3 = n1 + n2 #'+'调用__add__方法 
print(n3)

n4 = n3 - n2
print(n4)