#BMI指数

high = float(input("请输入身高（m）： "))
weight = int(input("请输入体重（kg）： "))

bmi = weight / high**2

if 0 < bmi < 18.5 :
    print("体重过轻")
elif 18.5 <= bmi <= 24:
    print("体重正常")
elif bmi > 24:
    print("体重过重")
else:
    print("输入不合理")

