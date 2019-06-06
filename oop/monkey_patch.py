# monkey patching
# means adding a new variable or method to a class after it's been defined.

class A(object):
    def __init__(self, num):
        self.num = num
    def __add__(self, other):
        return A(self.num + other.num)

def get_num(self):
    return self.num       

A.get_num = get_num  #monkey patching
foo = A(42)
bar = A(6);
foo = foo + bar
print(foo.get_num())