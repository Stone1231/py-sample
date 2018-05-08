#Importing an entire module
import functionEx 
import functionEx as fun #簡稱

print(functionEx.add(1,2,3))
print(fun.add(1,1,1))

#Importing a specific function
from functionEx import add
from functionEx import add as a #簡稱

print(add(1,1))
print(a(4,5))

#Importing all functions from a module
from functionEx import *
someName = get_full_name('jimi', 'hendrix') 
print(someName)