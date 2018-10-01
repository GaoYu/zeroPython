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
#       1) 写一个函数print_list(lst) 打印出所有元素
def print_list(lst):
    for L in lst:
        if type(L) is list:
            print_list(L)
        else:
            print(L)

#       2) 写一个函数 sum_list(lst) 返回这个列表中所有元素的和   
def sum_list(lst):
    s = 0
    for i in lst:
        if type(i) is list:
            s += sum_list(i)
        else:
            s += i
    return s

print_list(LL)
print("和是：",sum_list(LL))

