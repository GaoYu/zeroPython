#判断闰年
year = int(input("请输入一个年份： "))

if  year % 400 ==0:
    print(year,"是闰年")
elif year % 100 ==0:
    print(year,"不是闰年")
elif year % 4 == 0:
    print(year,"是闰年")

