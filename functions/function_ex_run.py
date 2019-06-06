#Importing an entire module
import function_ex 
import function_ex as fun #簡稱

print(function_ex.add(1,2,3))
print(fun.add(1,1,1))

#Importing a specific function
from function_ex import add
from function_ex import add as a #簡稱

print(add(1,1))
print(a(4,5))

#Importing all functions from a module
from function_ex import *
someName = get_full_name('jimi', 'hendrix') 
print(someName)