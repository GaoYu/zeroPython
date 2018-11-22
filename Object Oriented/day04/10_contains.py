


# 此示例示意in/not in运算符的重载
class MyList:
    def __init__(self, iterable):
        print("__init__被调用")
        self.data = list(iterable)

    def __repr__(self):
        return 'MyList(%r)' % self.data

    def __neg__(self):
        '''此方法用来制定 - self 返回的规则'''
        #L = [-x for x in self.data]
        L = (-x for x in self.data)
        return MyList(L)

    def __contains__(self, e):
        '''此方法用来实现in/not in 运算符重载'''
        print("__contains__被调用")
        for x in self.data:
            if x ==e:
                return True
        return False

L1 = MyList([1, -2, 3, -4])

if -2 in L1:
    print('-2 在L1中')
else:
    print('-2 不再L1中')
#当MyList的类内重载了__contains__方法，not in 也可以用
if -3 not in L1:
    print("-3不再L1中")
else:
    print("-3再L1中")