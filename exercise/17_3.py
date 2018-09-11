  #3. 完全数:
  #  1 + 2 + 3 = 6 (6为完全数)
  #  1, 2, 3 都为 6的因数(能被一个数x整数的数为y,则y为x的因数)
  #  1 x 6 = 6
  #  2 x 3 = 6
  #  完全数是指除自身以外，所有的因数相加之和等于自身的数
  #  求 4 ~ 5个完全数并打印
  #  答案:
  #    6
  #    28
  #    496
  #    ....
#方法1
#i = 1
#while True:
#    #判断是否是完全数，如果是则打印
#    L = [] #每次循环开始都创建一个新列表
#    for x in range(1, i):
#        if i % x == 0 :  #如果x是i的因数
#            L.append(x)  #放入列表
#    #此时L列表是i所有因素
#    if i == sum(L) :
#        print(i,"是完全数")
#    i += 1

#方法2，增加程序的可读性
def is_perfect_number(i):
    L = []
    for x in range(1, i):
        if i % x ==0:
            L.append(x)
    if sum(L) == i:
        return True
    return False

def main():
    i = 1
    while True:
        if is_perfect_number(i) :
            print(i,"是完全数")
        i += 1

main()