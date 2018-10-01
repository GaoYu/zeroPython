'''此模块示意模块内的隐藏属性
'''

def f1():
    pass

def _f2():
    #掩藏，from  import * 不会被导入
    pass

var1 = 'hello'

_var2 = 'world'