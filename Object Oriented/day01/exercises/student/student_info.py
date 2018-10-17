#练习:
#  1. 把学生管理系统划分为模块（把相关操作放在一个模块内）:
#    建议:
#       main.py 放主事件循环
#       menu.py 放show_menu函数
#       student_info.py 放学生信息相关的操作

#1)此函数添加学生信息，并返回学生信息的字典的列表
import os
os.chdir('C:/Users/yugao/zeroPython-master/Object Oriented/day01/exercises/student')

#导入学生类
from student import Student

def input_student():
    L = []
    while True:
        #字典容易被更新，只能放在循环里面
        name = input("学生姓名：")
        if not name:
            break
        age = int(input("学生年龄："))
        score = int(input("学生成绩："))

        d = Student(name, age, score)
        #stud = {}
        #stud['name'] = names
        #stud['age'] = ages
        #stud['score'] = scores
    
        L.append(d)
    return L

#2) 查看所有学生信息  
def output_student(L):
    print('+----------+----------+----------+')
    print('|    name  |   age    |   score  |')
    print('+----------+----------+----------+')

    for d in L:  #d绑定的是元组
        t = (d.name.center(10), 
             str(d.age).center(10), 
             str(d.score).center(10))
        line = "|%s|%s|%s|" % t   #t是元组
        print(line)

#4) 此函数用来存修改学生的成绩信息
def modify_student_info(lst):
    name = input("请输入要修改学生的姓名： ")
    for d in lst:
        if d['name'] == name:
            score = int(input("请输入新的成绩： "))
            d['score'] = score
            print("修改",name,'的成绩为',score)
            return
    else:
        print("没有找到名为：",name,'的学生信息')


#5) 删除学生信息的函数
def delete_student_info(lst):
    name = input("请输入要删除学生的姓名： ")
    for i in range(len(lst)): #从0开始把所有索引遍历一遍        
        if lst[i]['name'] == name:
            del lst[i]
            print("已成功删除", name)
            return True
    else:
        print("没有找到名为：",name,"的学生信息")

# 5)  按成绩从高至低打印学生信息
#   print("按成绩从高到低排序后")
def get_score_rev(lst):
    L = sorted(lst, key = lambda d : d['score'], reverse = True)
    return output_student(L)
# 6)  按成绩从低至高打印学生信息
def get_score(lst):
    L = sorted(lst, key = lambda d : d['score'])
    return output_student(L)

# 7)  按年龄从大到小打印学生信息
#print("按年龄从大到小排序后")
def get_age_rev(lst):    #d为字典
    L = sorted(lst, key = lambda d : d['age'], reverse = True)
    return output_student(L)
# 8)  按年龄从小到大打印学生信息
def get_age(lst):    #d为字典
    L = sorted(lst, key = lambda d : d['age'])
    return output_student(L)

# 9)  保存信息到文件(si.txt)
def save_to_file(lst, filename='si.txt'):
    '''将列表存储在numbers.txt文件中'''
    try:
        f = open(filename,'wt')
        for n in lst:
            for key,value in n.items():
                f.write('"'+key+'"'+':'+str(value))
                f.write(',')
                
            f.write('\n')
        f.close()
    except OSError:
        print("结束输入")

#       10) 从文件中读取数据(si.txt)
def read_from_file(filename='si.txt', mode='rt'):
    '''读取文件存入列表'''
    L = []
    #读取文件信息，形成元组后放入L
    try:
        f = open(filename, 'rt')

        while True:
            #读取数据
            s = f.readline()
            s = s.rstrip()
            s = s.rstrip(',')
            if not s:
                break       

            L.append(s)

        return L
        f.close()
    except OSError:
        print("打开文件失败！")

        