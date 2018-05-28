
print("====__builtins__====")
items = dir(__builtins__)
for item in items:
    print(item)

print(help(max))        

import math
print("====dir(math)====")
for item in dir(math):
    print(item)    

print(help(math.asin))

print(math.__doc__)

class Demo:
    """
Demo - 
        learning Python class..."""
 
    def __init__(self, i):
        self.i = i
     
    def __str__(self):
        return str(self.i)
          
    def hello(self):
        """This is a function that say hello"""
        print("hello", self.i)

    def hello2(self, name, language="en"):
        """Say hello to a person.
        Args:
        name: the name of the person as string
        language: the language code string
        Returns:
        A number.
        """
        print(language+" "+name)        

a = Demo(1122)
a.hello()
a.hello2("xxx","en")
print(a.__doc__) 
print("====Demo====")
help(Demo)    
print("====Demo.hello====")
help(Demo.hello) #同 help(a.hello)
help(Demo.hello2)

