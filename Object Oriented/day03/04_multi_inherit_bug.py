#04_multi_inherit_bug.py


#小张写了一个类A
class A:
    def m(self):
        print("A.m()被调用")

#小李写了一个类B
class B:
    def m(self):
        print("B.m()被调用")

#小王感觉小张和小李写的两个类自己可以使用

class AB(B, A):
    pass

ab = AB()
ab.m()          #请问调用谁,和顺序有关了？