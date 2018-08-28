#输入2个整数，第一个用begin绑定，第二个用end变量绑定，打印出begin~end的所有整数

begin = int(input("请输入第一个整数： "))
end = int(input("请输入第二个整数： "))
i = begin

while   i <=end :
    print(i)
    i += 1
else:
    print("输入不合法")

print("程序结束！ i=", i)
