#输入一个整数用begin绑定，在输入一个整数用end绑定，打印出从begin~end（包含end）的所有的偶数
#建议用continue语句跳过所有的奇数


begin = int(input("输入一个整数： "))
end  = int(input("输入一个整数： "))

for x in range(begin, end+1):
    if x % 2 != 0:
        continue
    print(x)


