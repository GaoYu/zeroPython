#

#此示例以建房子为例，说明什么情况使用异常处理机制

def f1():
    print("开始给房子打地基")
    #raise ValueError("地下出现文物")
    print("地基建完")
    return 0

def f2():
    print("开始建地面以上部分")
    #raise ValueError("地上要修高压线")
    print("高楼建完")

def f3():
    f1()
    f2()

def built_house():
    f3()


try:
    built_house()#开始建房子
except ValueError as err:
    print("房子没建完", err)

else:
    print("房子建完了")

    