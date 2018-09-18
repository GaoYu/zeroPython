#永远循环自身
import time
def story():
    time.sleep(5)
    print("从前有座山")
    print("山上有座庙")
    print("庙里有个老和尚讲故事：")
    story() #直接调用自身 
story()

#函数间调用自身递归
def fa():
    fb()
def fb():
    fa()
fa()
print("递归结束") #永远打印不了



def fx(n):
    print("递归进入第", n, "层")
    if n ==3:
        return
    fx(n + 1)
    print("递归退出第", n, '层')
fx(1)
print("程序结束")