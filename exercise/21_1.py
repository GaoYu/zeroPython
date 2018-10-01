#练习：
#  写一个程序，输入你的出生日期
#    1) 算出你已经出生了多少天?
#    2) 算出你出生那天是星期几?

#方法一

import time
#输入你的出生日期
year = int(input("请输入年： "))
month = int(input("请输入月： "))
day = int(input("请输入日： "))

#得到出生时的秒数
birthday_second = time.mktime((year,month,day,0,0,0,0,0,0))
#得到当前时间的秒数
cur_second = time.time()

#算出你已经出生多少天？
s = cur_second - birthday_second
print("您已出生：", s / 60 / 60 // 24)

#2)算出出生那天是星期几？
birthday = (year, month, day, 0, 0, 0, 0, 0, 0)
#转为秒数
s = time.mktime(birthday)
#转回本地时间元组
t = time.localtime(s)
weekday = {
    0:"星期一",
    1:"星期二",
    2:"星期三",
    3:"星期四",
    4:"星期五",
    5:"星期六",
    6:"星期日"
    }
print("您出生那天是：",weekday[t[6]])







#方法二
#1.判断一年是闰年
#判断闰年
def is_leapyear(year):
    if  year % 400 ==0 or ( year % 100 !=0 and year % 4 == 0):
        return True
    return False
#今天日期
import time    
#判断1900年1月1日至今多少天，1900年1月1日至出生日期多少天
def caculate_1900_days():
    #当期日期，年、月、日
    strDate = time.strftime('%Y%m%d', time.localtime(time.time())) #这里格式是‘%Y-%m-%d’。
    current_year = int(strDate[:4])
    current_month = int(strDate[4:6])
    current_day = int(strDate[6:])
    c_days = int(time.strftime('%j',time.localtime(time.time())))

    #出生日期、年月日
    birthDate = input("请输入出生日期： ") #格式为1990-12-01
    birth_year = int(birthDate.split('-')[0])
    birth_month = int(birthDate.split('-')[1])
    birth_day = int(birthDate.split('-')[2])
    b_days = int(time.strftime('%j',time.strptime(birthDate,'%Y-%m-%d')))

    w_days = time.strftime('%W',time.strptime(birthDate,'%Y-%m-%d'))

    #基准日期，年月日
    benchmarkDate = '1900-01-01' #格式为1990-12-01
    bench_year = int(benchmarkDate.split('-')[0])
    bench_month = int(benchmarkDate.split('-')[1])
    bench_day = int(benchmarkDate.split('-')[2])

    currentdays = (current_year - bench_year) * 365
    birthdays = (birth_year - bench_year) * 365

    for tempYear in range(bench_year, current_year, 1):
        if is_leapyear(tempYear):
            currentdays += 1
    for tempYear in range(bench_year, birth_year, 1):
        if is_leapyear(tempYear):
            birthdays += 1
    days = (currentdays + c_days) - (birthdays + b_days)
    return days
caculate_1900_days()

