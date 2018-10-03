
#练习：
#　　写一个生成器函数myodd(x) 来生成一系列奇数
#  如:
#    myodd(10) 可以生成 1 3 5 7 9

def myodd(x):
    i = 0
    while i < x:
        if i % 2 == 1:
            yield i 
        i += 1

for x in myodd(10):
    print(x)