#练习:
#  与一个函数 get_score() 来获取学生的成绩(0~100), 如果输入出现异常，则此函数返回0,否则返回用户输入的成绩
#  def get_score():
#      ....
#  score = get_score()
#  print("学生的成绩是:", score)

#方法一
def get_score():
    s = int(input("请输入成绩： "))
    if 0 <= s <= 100:
        return s
    return 0

try:
    score = get_score()
except:
    score = 0
print("学生的成绩是:", score)

#方法二
def get_score():
    try:
        s = int(input("请输入成绩： "))
    except ValueError:
        return 0

    if 0 <= s <= 100:
        return s
    return 0

score = get_score()
print("学生的成绩是：", score)