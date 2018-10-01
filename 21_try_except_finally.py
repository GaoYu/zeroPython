
#21_try_except_finally.py

#此示例示意try-except语句的用法

def div_apple(n):
    print('%d个苹果您想分给几个人？' % n)
    s = input('请输入人数： ')
    #<<=可能触发ValueError错误异常
    cnt = int(s)  
    #<<==可能触发ZeroDivisionError错误异常
    result = n/cnt 
    print("每个人分了",result, '个评估')

#以下是调用者
#用try-except语句捕获并处理ValueError类型的错误

try:
    print("开始分平台")
    div_apple(10)
    print("分苹果完成")
except ValueError:
    print("值错误，已处理")
finally:
    print("我是finally字句，我一定会被执行！")

print("程序正常退出")
