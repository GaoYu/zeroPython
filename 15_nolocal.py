var = 100
def f1():
    var = 200
    print("f1里的var=", var)
    def f2():
        var = 300      #此处要想修改f1里的var变量怎么办？
        print("f2里的var=", var)
    f2()

    print("f2调用结束后的var值为", var)

f1()
print("全局里的var=", var)

############################
#nonlocal语句只能在被嵌套函数内部使用
var = 100
def f1():
    var = 200
    print("f1里的var=", var)
    def f2():
        global var
        var = 300      #此处要想修改f1里的var变量怎么办？
        print("f2里的var=", var)
    f2()

    print("f2调用结束后的var值为", var)

f1()
print("全局里的var=", var)


############################
#访问nonlocal变量将对外面嵌套函数的作用域的变量进行操作
var = 100
def f1():
    var = 200
    print("f1里的var=", var)

    def f2():
        nonlocal var
        var = 300      #此处要想修改f1里的var变量怎么办？
        print("f2里的var=", var)
    f2()

    print("f2调用结束后的var值为", var)

f1()
print("全局里的var=", var)



############################
#当有两层或两层以上的函数嵌套时，访问nonlocal变量只对最近一层的变量进行操作
def f1():
    v = 100
    def f2():
        v = 200
        def f3():
            nonlocal v
            v += 1
        f3()
        print("f2最后的v=", v)
    f2()

    print("f1最后的v=", v)

f1()
print("全局里的v=", v)



############################
#nonlocal语句的变量列表里的变量名，不能出现在此函数的参数列表中
def f1():
    v = 100
    def f2(v):             #报错
        #nonlocal v        #报错
        v += 1
    f2(20)
f1()
