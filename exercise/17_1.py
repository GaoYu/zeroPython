#编写一个函数myfun,此函数用显示两个参数的相关信息函数
#def myfun(a, b)
#此处自己实现
#此函数给定两个参数，打印关于两个参数的信息：
#1）打印两个参数的最大值
#2）打印两个参数的和
#3）打印两个参数的积
#4）打印从a开始到b结束的所有偶数
#如：
#myfun(3,10)
#打印如下：
#最大值是：10
#和是：13
#积是：30
#3到10之间的偶数是4 6 8


def myfun(a, b):
    print("最大值是：",max(a,b))
    print("和是：",a + b)
    print("积是：",a * b)
    y = [x for x in range(a,b) if x % 2 == 0]
    print(a,"到",b,"之间的偶数是：", y)


