#练习:
#  实现两个自定义列表相加:
#    class MyList:
#        def __init__(self, iterable):
#            self.data = list(iterable)
#        .... 以下自己实现

#    L1 = MyList([1, 2, 3])
#    L2 = MyList([4, 5, 6])
#    L3 = L1 + L2
#    print(L3)  # MyList([1,2,3,4,5,6])
#    L4 = L2 + L1
#    print(L4)  # MyList([4,5,6,1,2,3])
#    L5 = L1 * 2
#    print(L5)  # MyList([1,2,3,1,2,3])

class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)
    
    def __add__(self, rhs):
        v = self.data + rhs.data
        return MyList(v)

    def __mul__(self, rhs):
        v = self.data * rhs
        return MyList(v)

    def __repr__(self):
        return 'MyList(%r)' % self.data

L1 = MyList([1, 2, 3])
L2 = MyList([4, 5, 6])
L3 = L1 + L2
print(L3)  # MyList([1,2,3,4,5,6])
L4 = L2 + L1
print(L4)  # MyList([4,5,6,1,2,3])
L5 = L1 * 2
print(L5)  # MyList([1,2,3,1,2,3])