#练习：
#  猜数字游戏:
#    写程序，随机生成一个0~100之间的数用变量x绑定
#    循环让用户输入一个数用y绑定,
#       输出猜数字的结果
#         1. 如果y等于生成的数x,则提示"您猜对了", 打印出猜测的次数并退出
#         2. 如果y 小于x则提示"您猜小了"，然后继续猜
#         3. 如果y 大于x则提示"您猜大了"，然后继续猜
#    猜对后程序退出并打印次数
import sys
import random as R

x = R.randrange(101)

times = 0
while True:
    y = int(input("请输入一个数"))
    times +=1
    if y < x :
        print("您猜小了")
    elif y > x:
        print("您猜大了")
    else:
        print("您猜对了")
        break

print("您共猜了%d次" % times)



