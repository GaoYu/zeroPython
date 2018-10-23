#10_override.py

# 此示例示意覆盖的用法

class A:
    def work(self):
        print("A.work()被调用")

class B(A):
    '''B类继承A类'''
    def work(self):
        print("B.work()被调用")

b = B()
b.work()  #请问执行结果

a = A()
a.work()  #请问执行结果是什么？

