#while.py

#此示例为while语句用法

i = 1 #创建一个变量，用来控制while循环的次数

while i < 20 : #判断循环条件，如果为真则执行语句块
    print("hello world!")
    i += 1 #修改循环变量
else:
    print("条件不满足，循环结束！")

print("上一条while预计结束，此时变量i =", i)
