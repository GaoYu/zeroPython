#不能先声明局部变量，再经过global声明为全局变量，此做法不符合规则

def f1():
    #x = 100
    global x
    x = 100

f1()

#global变量列表里的变量不能出现在此作用域内的形参列表里面
v = 100
def f2(v):
    #global v   #形参列表，global
    v = 300
f2(200)
print(v)