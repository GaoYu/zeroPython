# 打印如下宽度的正方形：

# 1 2 3 4
# 2 3 4 5
# 3 4 5 6
# 4 5 6 7

n = int(input("请输入： "))
for y in range(1, n + 1): 
    for x in range(y, y + n):
        print("%2d" % x, end = " ")
    print()    
