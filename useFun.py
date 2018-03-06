#Importing an entire module
import functions 
import functions as fun #簡稱

print(functions.add(1,2,3))
print(fun.add(1,1,1))

#Importing a specific function
from functions import add
from functions import add as a #簡稱

print(add(1,1))
print(a(4,5))

#Importing all functions from a module
from functions import *
someName = get_full_name('jimi', 'hendrix') 
print(someName)