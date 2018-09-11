#猴子吃桃
#有一只小猴子，摘了很多桃
#  第一天吃了全部桃子的一半，感觉不饱又吃了一个
#  第二天吃了剩下的一半，感觉不饱又吃了一个
#  ...
#  依此类推
#  到第十天，发现还剩一个了
#  请问第一天摘了多少桃？

#方法1
def myfun(n):
    for x in range(10000):
        if x / 2**(n-1) - (1 + (2**(n-2) - 1)/2**(n-2)) == 1:
                                 return x
        
myfun(10)        


#方法2

#根据今天的桃子数计算昨天的桃子数
def get_last(y):
    x = 2 * (y + 1)
    return x

p = 1 #第十天的桃子数
#day9 = get_last(1)
#day8 = get_last(day9)

day = 10       #用来表示当前是第几天
while day > 1:#
    day -= 1
    p = get_last(p)
    print("第",day,"天的桃子树是：",p)


