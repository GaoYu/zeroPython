#练习:

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


LL = [[3,5,8], 10, [[13, 14], 15, 18], 20]
print(L)

#       1) 写一个函数print_list(lst) 打印出所有元素
def print_list(lst):
    for L in lst:
        if type(L) is list:
            print_list(L)
        else:
            print(L)
print_list(L)

#       2) 写一个函数 sum_list(lst) 返回这个列表中所有元素的和   

L = []
def sum_list(lst):
    for i in lst:
        if type(i) is int:
            L.append(i)
        else:
            sum_list(i)
  
sum_list(LL)
L
sum(L)
