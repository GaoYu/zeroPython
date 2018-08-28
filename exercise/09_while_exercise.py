#利用while预计解决，输入一个数，打印n行“hello world!”

n = int(input("输入一个数： "))

i = 1

#方法一
#while i <= n  :
#    print('hello world!')
#    i += 1
#else:  #可以省略
#    print("条件不满足， 循环结束！")


#方法二，直接用变量n来控制
while 1 <= n:
    print('hello world!')
    n -= 1
    





print("程序结束！ n=",n)
