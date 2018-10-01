#mymod5.py

'''此模块示意__name__属性的作用
'''

def f1():
    print("f1被调用")

if __name__ == '__main__':
    print("mymod5.py正在当作主模块运行")
    f1()
else:
    print("mymod5.py正在被其他模块导入！！")
    print("模块名为：",__name__)