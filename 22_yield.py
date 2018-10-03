#yield.py

#此示例示意生成器函数的定义及使用（没有return也不会返回None）
def myyield():
    '''此函数为生成器函数'''
    print("即将生成2") #只有next才会执行
    yield 2  #生成2
    print("即将生成3")
    yield 3  #生成3
    print("即将生成5")
    yield 5  #生成5
    print("myyield函数返回")  
#用for 语句访问myyield函数

for x in myyield():
    print(x)

gen = myyield()
it = iter(gen)
next(it)
next(it)
next(it)
next(it)