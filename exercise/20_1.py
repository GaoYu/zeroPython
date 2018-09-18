#练习:
#   1. 编写函数求阶乘 myfac(x), 用什么方法都可以
#   2. 写程序算出1~20的阶乘的和
#     1!+2!+3!+.....+20!
#   3. 改写之前学生信息管理程序，添加如下四个功能
#     5)  按成绩从高至低打印学生信息
#     6)  按成绩从低至高打印学生信息
#     7)  按年龄从大到小打印学生信息
#     8)  按年龄从小到大打印学生信息
#     (要求原来输入的列表顺序保持不变)
#   4. 已知有列表:
#     L = [[3,5,8], 10, [[13, 14], 15, 18], 20]
#       1) 写一个函数print_list(lst) 打印出所有元素
#         print_list(L)  # 打印 ....
#       2) 写一个函数 sum_list(lst) 返回这个列表中所有元素的和
#    注:
#      type(x) 可以返回一个变量的类型
#      如:
#          type(20) is int        # 返回True
#          type([1,2,3]) is list  # 返回True


#   1. 编写函数求阶乘 myfac(x), 用什么方法都可以
import math
from functools import reduce
def myfac(n):
    ##1.递归
    #if n ==1:
    #    return 1
    #return n * myfac(n-1)
    #2.factorial 函数
    #return math.factorial(n)
    #3.reduce函数
    return reduce(lambda x,y:x*y,range(1,n+1))
myfac(4)
myfac(5) 
#   2. 写程序算出1~20的阶乘的和
#     1!+2!+3!+.....+20!

def sum_myfac(n):
    #1.循环调函数
    #s = 0
    #for i in range(1,n+1):
    #    s +=myfac(i)
    #return s
    #2.函数式
    return sum(map(myfac,range(1,n+1)))

sum_myfac(2)
