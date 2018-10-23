
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

    for d in L:  
        n, a, s = d.get_infos()
        t = (n.center(10), 
             str(a).center(10), 
             str(s).center(10))
        line = "|%s|%s|%s|" % t   #t是元组
        print(line)

#4) 此函数用来存修改学生的成绩信息
def modify_student_info(lst):
    name = input("请输入要修改学生的姓名： ")
    for d in lst:
        #if d['name'] == name:
        if d.is_name(name):

            score = int(input("请输入新的成绩： "))
            #d['score'] = score设置成绩
            d.set_score(score)
            print("修改",name,'的成绩为',score)
            return
    else:
        print("没有找到名为：",name,'的学生信息')


#5) 删除学生信息的函数
def delete_student_info(lst):
    name = input("请输入要删除学生的姓名： ")
    for i in range(len(lst)): #从0开始把所有索引遍历一遍        
        #if lst[i]['name'] == name:
        if lst[i].is_name(name):
            del lst[i]
            print("已成功删除", name)
            return True
    else:
        print("没有找到名为：",name,"的学生信息")

# 5)  按成绩从高至低打印学生信息
#   print("按成绩从高到低排序后")
def get_score_rev(lst):
    L = sorted(lst, 
               key = lambda d : d.get_score(), 
               reverse = True)
    return output_student(L)
# 6)  按成绩从低至高打印学生信息
def get_score(lst):
    L = sorted(lst, 
               key = lambda d : d.get_score())
    return output_student(L)

# 7)  按年龄从大到小打印学生信息
#print("按年龄从大到小排序后")
def get_age_rev(lst):    #d为字典
    L = sorted(lst, 
               key = lambda d : d.get_age(), 
               reverse = True)
    return output_student(L)
# 8)  按年龄从小到大打印学生信息
def get_age(lst):    #d为字典
    L = sorted(lst, key = lambda d : d.get_age())
    return output_student(L)

# 9)  保存信息到文件(si.txt)
def save_to_file(docs, filename='si.txt'):
    '''将列表存储在si.txt文件中'''
    try:
        f = open(filename,'wt')
        for stu in docs:
            #n, a, s = stu.get_infos()
            stu.write_to_file(f)
        f.close()
        print("保存文件成功")
    except OSError:
        print("保存失败")

#       10) 从文件中读取数据(si.txt)
def read_from_file(filename='si.txt', mode='rt'):
    '''读取文件存入列表'''
    L = []
    try:
        f = open(filename, 'rt')

        for line in f:
            s = line.rstrip()#去掉右侧换行符
            lst = s.split(',')  #得到列表['姓名','年龄','成绩']
            name, age, score = lst
            age = int(age)
            score = int(score)
            L.append(Student(name, age, score))

        f.close()
    except OSError:
        print("打开文件失败！")

    return L

        