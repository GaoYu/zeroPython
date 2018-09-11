#模拟一个点名系统，已知全班同学名单，随机打印学生的姓名进行点名，并得到此学生是否已到的信息，
#输入‘y’代表到了，其他输入代表未到场。
#点名结束后打印未到者名单

names = ['tom', 'jerry', 'spike', 'tyke']
s = set(names)

L = []         #存放未到人名单
for n in s:
    info = n + " 已到？（y）："
    r = input(info)
    if  r != 'y':
        L.append(n)

print("未到人的名单如下：")
for n in L:
    print(n, end= " ")
print()


