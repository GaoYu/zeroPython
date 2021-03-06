#21_try_except.py

#此示例示意try-except语句的用法

def div_apple(n):
    print('%d个苹果您想分给几个人？' % n)
    s = input('请输入人数： ')
    #<<=可能触发ValueError错误异常
    try:
        cnt = int(s)  
        #<<==可能触发ZeroDivisionError错误异常
        result = n/cnt 
        print("每个人分了",result, '个评估')
    except ZeroDivisionError:
        print("被零除错误！")

#以下是调用者
#用try-except语句捕获并处理ValueError类型的错误

try:
    print("开始分平台")
    div_apple(10)
    print("分苹果完成")
#except ValueError:
#    print("div_apple内出现了ValueError错误,已处理")
#    print("用户输入不合法，苹果退回来不分了")
#except ZeroDivisionError:
#    print("出现被0除的错误！苹果不分了")

except (ValueError, ZeroDivisionError):
    print("苹果不分了")


print("程序正常退出")