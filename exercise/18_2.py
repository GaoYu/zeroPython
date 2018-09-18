#    2. 修改之前的学生信息管理程序:
#      编写两个函数用于封装 录入学生信息　和　打印学生信 息的功能
#        1) 
#        def input_student():
#        　　　　#此函数获取学生信息，并返回学生信息的字典的列表
#            ....
#        2. 
#        def output_student(L):
#            # 以表格形式再打印学生信息
#            ...
#      验证测试：
#      　　L = input_studnet()
#        output_student(L)
#        print("再添加几个学生信息")
#        L += input_student()
#        print("添加学生后的学生信息如下:")
#        output_student(L)


#1.此函数获取学生信息，并返回学生信息的字典的列表
def input_student():
    L = []
    while True:
        stud = {}                   #字典容易被更新，只能放在循环里面
        names = input("学生姓名：")
        if not names:
            break
        ages = int(input("学生年龄："))
        scores = int(input("学生成绩："))
        stud['name'] = names
        stud['age'] = ages
        stud['score'] = scores
    
        L.append(stud)
    return L




#2.以表格形式再打印学生信息
def output_student(L):
    print('+----------+----------+----------+')
    print('|    name  |   age    |   scire  |')
    print('+----------+----------+----------+')

    for d in L:  #d绑定的是元组
        t = (d['name'].center(10), 
             str(d['age']).center(10), 
             str(d['score']).center(10))
        line = "|%s|%s|%s|" % t   #t是元组
        print(line)

#验证测试：
L = input_student()
output_student(L)
print("再添加几个学生信息")
L += input_student()
print("添加学生后的学生信息如下:")
output_student(L)
