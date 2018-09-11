  #2. 学生管理项目准备工作:
  #   写一个程序，任意输入n个学生的信息,形成字典后存于列表中:
  #     学生的信息包括:
  #        姓名(字符串)
  #        年龄(整数)
  #        成绩(整数)
  #   循环输入学生信息，直到输入学生姓名为空时结束输入,
  #   最后形成字典列表如下:
  #     L = [
  #          {'name':'xiaozhang', 'age':20, 'score': 100},
  #          {'name':'xiaoli', 'age':21, 'score': 98},
  #          {'name':'xiaowang', 'age':19, 'score': 89},
  #          ...
  #     ]
  #  2) 将以上列表显示为如下的表格:
  #  +------------+------+-------+
  #  |   name     | age  | score |
  #  +------------+------+-------+
  #  | xiaozhang  |  20  |  100  |
  #  |  xiaoli    |  21  |   98  |
  #  | xiaowang   |  19  |   89  |
  #  +------------+------+-------+



###第一步，形成字典，读取学生信息





#t  =('name', 'ages', 'score')
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

#print(L)


  #  2) 将以上列表显示为如下的表格:

print('+----------+----------+----------+')
print('|    name  |   age    |   scire  |')
print('+----------+----------+----------+')

for d in L:  #d绑定的是元组
    t = (d['name'].center(10), 
         str(d['age']).center(10), 
         str(d['score']).center(10))
    line = "|%s|%s|%s|" % t   #t是元组
    print(line)

