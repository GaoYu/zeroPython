#str_format.py

fmt= "姓名：_%s_, 年龄：_%d_"

name = input('请输入姓名： ')
age = int(input('请输入年龄： '))

s = fmt %(name, age)

print(s)