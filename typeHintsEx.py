from typing import Dict, Tuple, List, Callable, NamedTuple

#ex1
def two_sum(a: int, b: int) -> int:
    return a + b

print(two_sum.__annotations__)    

print(two_sum(2, 1)) # result: 3

#Class ex
class Point():  
    def __init__(self, x, y): 
        self.x = x 
        self.y = y

def output_point(point:Point):
    print(point.x)

output_point(Point(1,3))

# NamedTuple ex
Point2 = NamedTuple('Point2', x=int, y=int)

def output_point2(point:Point2):
    print(point.x)

output_point2(Point2(2,4))       


#ex Dict, Tuple, List
ConnectionOptions = Dict[str, str]
Address = Tuple[str, str]
Server = Tuple[Address, ConnectionOptions]

def broadcast_message(message: str, servers: List[Server]) -> None:
    for server in servers:
        print(server)    
    print(message)

broadcast_message("hi!",[("a","b"),("c","d")])