#ex1
def two_sum(a: int, b: int) -> int:
    return a + b

print(two_sum.__annotations__)    

print(two_sum(2, 1)) # result: 3

# class ex
class Point():  
    def __init__(self, x, y): 
        self.x = x 
        self.y = y

def output_point(point:Point):
    print(point.x)

output_point(Point(1,3))

# NamedTuple ex
import typing
Point2 = typing.NamedTuple('Point', x=int, y=int)

def output_point2(point:Point2):
    print(point.x)

output_point2(Point(2,4))       

  