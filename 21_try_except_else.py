
#21_try_except_as.py

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
except:
    print("错误被捕获")
else:
    print("程序正常，没有发现异常")

print("程序正常退出")
