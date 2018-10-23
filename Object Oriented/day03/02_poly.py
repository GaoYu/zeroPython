#02_poly.py

#此示例示意多态：

class Shape:
    def draw(self):
        print("Shape.draw被调用")

class Point(Shape):
    def draw(self):
        print('正在画一个点')

class Circle(Point):
    def draw(self):
        print('正在画一个圆')

def my_draw(s):
    s.draw()           #此处调用哪个方法呢？#显示多态中的动态


s1 = Circle()
s2 = Point()

my_draw(s1)            #调用Circle里的draw
my_draw(s2)            #调用Point里的draw