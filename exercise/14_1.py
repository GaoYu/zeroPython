#输入一个整数，代表树干的高度
#打印一颗“圣诞树”
#如：
#输入2
#打印
# *
#***
# *
# *
#输入：3
#打印
#     *
#    *** 
#   *****
#     *
#     *
#     *

n = int(input("圣诞树的高位： "))
#方法一
#打印树叶
#for i in range(1, n + 1):                 #i从上向下的行
#    blanks_count = n - i               #计算空格数
#    print(" " * blanks_count + "*" * (2*i - 1)
#打印树干
#for i in range(1, n + 1):
#    print(" " * (n -1) + '*')
          
for i in range(1,2*n,2):
    line = "*"* i
    print(line.center(2*n - 1))

for j in range(n):
    print("*".center(2*n - 1))



##用循环语句生成如下字符串：
# 'ABC.....XYZ'
#'AaBaCc.....XxYyZz'
#提示，ord和chr函数结合循环语句实现
#for i in range(65,91):
#    print(chr(i), end="")
#for i in range(65,91):
#    print(chr(i)+chr(i+32), end="")
s = ''
s2 = ''
for i in range(65, 65 + 26):
    s += chr(i)
    s2 += chr(i)
    s2 +=chr(i + 32)
print(s)
print(s2)


##算出100~999以内的水仙花数；
#水仙花数是指百位的3次方加上十位的3次方加上个位的3次方等于原数的数字
#例数：153 = 1 **3 + 5**3 + 3**3


#方法一
for x in range(1,10):
    for y in range(10):
        for z in range(10):
            n = x * 100 + y * 10 + z
            if n == x**3 + y**3 + z**3:
                print(n)

#方法二
for x in range(100,1000):
    bai = x // 100
    shi = x % 100 //10
    ge = x % 10
    if x == bai **3 + shi **3 + ge ** 3:
        print(x)
