#练习:
#  1. 求 1 ** 2 + 2 ** 2 + 3 ** 2 + ... + 9**2 的和
#方法1
def pow2(x):
    return x ** 2
print(sum(map(pow2, range(1,10)))

#方法2
print(sum(map(lambda x : x ** 2, range(1,10))))

#  2. 求 1 ** 3 + 2 ** 3 + 3 ** 3 + ... + 9**3 的和
def fx():
    L = []
    for x in map(pow, range(1,10), [3]*9):
        L.append(x)
    return sum(L)
fx()
#方法2
print(sum(map(lambda x : x ** 3, range(1,10))))


#  3. 求 1**9 + 2**8 + 3**7 + ... + 9**1的和  # 11377
def fx():
    L = []
    for x in map(pow, range(1,10), range(9,0,-1)):
        L.append(x)
    return sum(L)
fx()

#方法2
print(sum(map(pow, range(1,10), range(9,0,-1))))
