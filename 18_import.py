#练习 ：
#  1. 输入一个正方形的周长，输出正方形的面积
#  2. 输入一个圆的半径，打印出这个圆的面积
#  3. 输入一个正方型的面积，打印这个正方型的周长
#  ( 要求: 用math模块内的函数和数据)

#导入math模块
import math as m

#问题1
def squre_area():
    l = float(input("请输入正方形的周长："))
    return m.pow(l/4,2)
squre_area()

#问题2
def circle_area():
    l = float(input("请输入圆的半径："))
    return m.pow(l,2)* m.pi
circle_area()
#问题3
def squre_circumference():
    l = float(input("请输入正方形的面积："))
    return m.sqrt(l)*4