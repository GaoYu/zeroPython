#练习：
#　　写一个生成器函数:
#    def myinteger(n):
#        ....
#    此生成器函数可以生成从0开始，的一系列的整数,到n结束(不包含n)

#    for x in myinteger(3):
#        print(x)   # 打印 0, 1, 2
#    it = iter(myinteger(2))
#    print(next(it))  # 0
#    print(next(it))  # 1
#    print(next(it))  # StopIteration异常

def myinteger(n):
    #for i in range(n):
    #    yield i
    i = 0
    while i < n:
        yield i 
        i+= 1


for x in myinteger(3):
    print(x)   # 打印 0, 1, 2
it = iter(myinteger(2))
print(next(it))  # 0
print(next(it))  # 1
print(next(it))  # StopIteration异常
