
f = lambda x : True if (x ** 2 + 1) % 5 == 0 else False
f(2)


f = lambda x, y: x if x > y else y



def fx(f, x, y):
    print(f(x, y))


fx(lambda x,y: x + y, 10 , 20)