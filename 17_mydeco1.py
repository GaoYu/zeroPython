#此示例示意函数装饰器的用法

#定义一个装饰器函数解决问题
def mydeco(fn):
    def fx():
        print('+++++++++++++++')
        fn()
        print('---------------')
    return fx


#定义函数的地方（小张写的）
@mydeco
def myfunc():    
    print("myfunc被调用")
    
#调用函数部分是小李写的
myfunc()
myfunc()
#调用函数的地方可能是小王写的
myfunc()
