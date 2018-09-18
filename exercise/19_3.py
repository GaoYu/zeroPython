#练习:
#    names = ['Tom', 'Jerry', 'Spike', 'Tyke']
#    让names排序
#      排序的依据是字符串的反序
#             'moT'    'yrreJ'  'ekipS'  'keyT'
#    L2 = sorted(names, ....) 
#    排序后:
#    L2 = ['Spike', 'Tyke', 'Tom', 'Jerry']

names = ['Tom', 'Jerry', 'Spike', 'Tyke']

def rev(name):
    return name[::-1]
sorted(names, key = rev)



#练习:
#   写函数input_student() 得到学生的姓名,成绩，年龄
#   output_student(L) 打印学生信息
#   (可以把以前的input_student/output_student函数直接拿过来用)

#   L = input_student()  # 输入一些学生信息
#   print("按年龄从大到小排序后")
#   L2 = sorted(L, .....)
#   output_student(L2)
#   print("按成绩从高到低排序后")
#   L3 = sorted(L, .....)
#   output_student(L3)

#输入学生信息
def input_student():
    L = []
    while True:                          
        names = input("学生姓名：")
        if not names:
            break
        ages = int(input("学生年龄："))
        scores = int(input("学生成绩："))
        stud = {} #字典容易被更新，只能放在循环里面
        stud['name'] = names
        stud['age'] = ages
        stud['score'] = scores
    
        L.append(stud)
    return L
#输出学生信息
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

L = input_student()  # 输入一些学生信息



#1.print("按年龄从大到小排序后")
def get_age(d):    #d为字典
    return d['age']     #返回字典中年龄
L2 = sorted(L, key = get_age, reverse = True)
output_student(L2)


#   print("按成绩从高到低排序后")
L3 = sorted(L, key = lambda d : d['score'], reverse = True)
output_student(L3)