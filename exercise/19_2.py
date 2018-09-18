#  4. 修改之前的学生信息管理程序，实现添加菜单和选择菜单操作功能:
#     菜单:
#       +-----------------------------+
#       |  1) 添加学生信息              |
#       |  2) 查看所有学生信息          |
#       |  3) 修改学生的成绩            |
#       |  4) 删除学生信息              |
#       |  q) 退出                     |
#       +-----------------------------+
#     请选择: 1
#       请输入姓名:....
#     请选择: 3
#       请输入修改学生的姓名: ....
#    (要求每个功能都对应一个函数)

#1)此函数添加学生信息，并返回学生信息的字典的列表
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

#2) 查看所有学生信息  
def output_student(L):
    print('+----------+----------+----------+')
    print('|    name  |   age    |   score  |')
    print('+----------+----------+----------+')

    for d in L:  #d绑定的是元组
        t = (d['name'].center(10), 
             str(d['age']).center(10), 
             str(d['score']).center(10))
        line = "|%s|%s|%s|" % t   #t是元组
        print(line)


#1.写一个打印菜单的函数
def show_menu():
    print('+-----------------------------+')
    print('|  1) 添加学生信息            |')
    print('|  2) 查看所有学生信息        |')
    print('|  3) 修改学生的成绩          |')
    print('|  4) 删除学生信息            |')
    print('|  q) 退出                    |')
    print('+-----------------------------+')


#2) 此函数用来存修改学生的成绩信息
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


#4) 删除学生信息的函数
def delete_student_info(lst):
    name = input("请输入要删除学生的姓名： ")
    for i in range(len(lst)): #从0开始把所有索引遍历一遍        
        if lst[i]['name'] == name:
            del lst[i]
            print("已成功删除", name)
            return True
    else:
        print("没有找到名为：",name,"的学生信息")


#4定义一个主函数，用来获取键盘操作，实现选择的工作
def main():
    docs = [] #此列表用来存储所有学生的信息字典
    while True:
        show_menu()
        s = input("请选择：")
        if s == '1':
            docs += input_student()
        elif s =='2':
            output_student(docs)
        elif s =='3':
            modify_student_info(docs)
        elif s=='4':
            delete_student_info(docs)
        elif s =='q':
            return #结束此函数执行，直接退出

main()