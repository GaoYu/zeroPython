#02_class_variable.py

#此实例示意类变量的用法

class Human:
    count = 0 #创建一个类变量

print("Human的类变量count=", Human.count)  #0
h1 = Human()
print("用h1对象访问Human的count变量", h1.count)  #0

h1.count = 100      #创建实例变量
print(h1.count)  #100
print(Human.count) #0
