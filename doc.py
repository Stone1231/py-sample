class Demo:
    """
Demo - 
        learning Python class..."""
 
    def __init__(self, i):
        self.i = i
     
    def __str__(self):
        return str(self.i)
          
    def hello(self):
        print("hello", self.i)

a = Demo(1122)
a.hello()
print()
print(a.__doc__)        