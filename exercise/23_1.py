#练习:
#  1. 一个球100米高空落下,每次落下后反弹高度是原高度的一半,再落下,
#  写程序
#    1) 算出皮球在第10次落地后反弹高度是多少,
#    2) 打印出球共经过了多少米的路程
  

def ball(height, times):
    '''根据原始给定的高度和反弹次数，返回反弹的高度'''
    for _ in range(times):
        height /= 2  #每次反弹是原来的一般
    return height

print("皮球从100m高度在第10次落地后反弹高度是:", ball(100, 10))

def ball_distance(height, times):
    s = 0 #用来累加所有路程
    for _ in range(times):
        s += height #把下落过程累加到s
        height /= 2
        s += height #把反弹高度累加到s
    return s

print("皮球从100m高度在第10次落地后经历的路程是：", ball_distance(100, 10))
    
