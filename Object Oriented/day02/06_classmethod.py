#05_classmethod.py

#此示例示意 类方法定义方法和用法

class Car:
    count = 0 #类变量
    @classmethod
    def getTotalCount(cls):
        '''此方法为类方法，第一个参数为cls，代表调用此方法的类'''
        return cls.count
    
    @classmethod
    def updateCount(cls, number):
        cls.count += number

    @classmethod
    def getInfo(cls):
        return cls.count
print(Car.getTotalCount())  #用类调用类方法 0


#Car.count += 1 #面向对象思想不提倡直接操作属性
print(Car.getTotalCount())  #1

c1 = Car()  #创建实例
c1.updateCount(100)  #Car实例也可以访问,类变量已经修改100
print(c1.getTotalCount())

c1.count = 200
v = c1.getInfo()  # 200 ? 100?类方法不能访问此类创建的实例的属性（只能访问类变量）
print(v)