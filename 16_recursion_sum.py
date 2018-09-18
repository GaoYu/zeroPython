#求和 1 + 2 +...+98 + 99 + 100

def mysum(x):
    if x <= 1: #设置递归终止点
        return 1
    return x + mysum(x - 1)

mysum(100)