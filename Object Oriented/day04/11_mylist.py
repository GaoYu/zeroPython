


# 此示例示意索引/切片运算符的重载
class MyList:
    def __init__(self, iterable):
        print("__init__被调用")
        self.data = list(iterable)

    def __repr__(self):
        return 'MyList(%r)' % self.data

    def __getitem__(self, i):
        print("__getitem__被调用, i= ",i)
        if type(i) is not int:
            raise TypeError
        return self.data[i]
    
    def __setitem__(self, i , v):
        print("__setitem__被调用， i=", i, 'v=', v)
        self.data[i] = v  #修改data绑定的元素


L1 = MyList([1, -2, 3, -4])

v = L1[0]

print(v)
#print(L1['HELLO'])


L1[1]  = 2  #等同于调用L1.__setitem__(1,2)

v = L1[1]
print(v)