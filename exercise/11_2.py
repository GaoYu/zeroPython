#写程序用while实现打印三角形。
#要求输入一个整数表示三角形的宽度和高度，打印出如下的三种直角三角形
#    *
#   **
#  ***
# ****

# ****
#  ***
#   **
#    *

# ****
# ***
# **
# *


n = int(input("输入一个整数： "))

i = 1

#while i <= n:
#    print(" "*(n - i)+ "*"*i)
#    i += 1

while i <= n:
    print(" "*(i - 1) + "*"*(n -i +1))
    i += 1
        
#while i <= n:
#    print("*"*(n -i +1) + " "*(i - 1))
#    i += 1

        
