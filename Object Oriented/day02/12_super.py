#12_super.py

# 此示例示意super的用法

class A:
    def work(self):
        print("A.work()被调用")

class B(A):
    '''B类继承A类'''
    def work(self):
        print("B.work()被调用")

    def super_work(self):
        #此处能调用父类的work方法吗？
        #self.work()  #B.work()
        #super(B, self).work() #A.work()
        #super(__class__ , self).work() #A.work()
        super().work() #A.work()

b = B()

#调用父类的work方法
#b.__class__.__base__.work(b) #A.work()被调用

super(B, b).work()  #调用超类的work方法

b.super_work()
