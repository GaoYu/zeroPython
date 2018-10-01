#mymod6.py


'''此模块示意__all__列表的用法
'''
#限制用from mymod6 import *时只导入f1,var1

__all__  = ["f1","var1"]

def f1():
    pass

def f2():
    pass

def f3():
    pass

var1 = "hello"
var2 = "world"