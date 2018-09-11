def myfun(a, b, c):
    print('a绑定的是：', a)
    print('b绑定的是：', b)
    print('c绑定的是：', c)

#位置传参
myfun(1, 2, 3)

#序列传参
s = [1, 2, 3]
myfun(*s)

#关键字传参

myfun(c = 3, b =2, a = 1)

#字典关键字传参

d = {'c':3, 'b':2, 'a':1}
