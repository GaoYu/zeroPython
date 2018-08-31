#输入一个整数n,判断这个整数是否是素数（prime)
#素数是只只能被1和自身整除的数
#如：2，3，5，7，11

#方法排除法，一旦n能被2-n-1的整数整除就不是素数


n = int(input("输入一个整数： "))
#方法一
#flag = True
#for x in range(2,n):
#    if n % x == 0 :
#        #print(n,"不是素数")
#        flag = False
#        break
#if flag == True:
#    print(n,'是素数')
#else:
#    print(n,'不是素数')


#方法二

for i in range(2, n):
    if n % i == 0:
        print(n,'不是素数')
        break
else:
    print(n,'是素数')


