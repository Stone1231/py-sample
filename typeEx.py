issubclass(bool, int) # True
isinstance(True, bool) # True
isinstance(False, bool) # True

#int: Integer number
ai = 2
bi = 100
ci = 123456789
di = 38563846326424324

#float: Floating point number
af = 2.0
bf = 100.e0
cf = 123456789.e1

# complex: Complex numbers
ac = 2 + 1j
bc = 100 + 10j

strs = reversed('hello')
# for s in strs:
#     print(s)

#tuple: An ordered collection of n values of any type (n >= 0).
at = (1, 2, 3)
bt = ('a', 1, 'python', (1, 2))
#bt[2] = 'something else' # returns a TypeError   

#list: An ordered collection of n values (n >= 0)
al = [1, 2, 3, 3]
# print(al[0]) # 1
# print(al[-1]) # 3
# print(al.count(3)) #2
bl = ['a', 1, 'python', (1, 2), [1, 2]]
bl[2] = 'something else' # allowed
cl = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
cl.append("Sia")
print(cl)
cl.insert(1, "Nikki")
print(cl)
cl.remove("Bob")
print(cl)
print(cl.index("Alice"))
print(len(cl))
print(cl[::-1]) #倒排
for s in reversed(cl):
    print(s)
print(cl.pop()) #Remove and return item at index 
                #(defaults to the last item) with L.pop([index]), 
                # returns the item
print(cl)


# set: An unordered collection of unique values. Items must be hashable.
aset = {1, 2, 'a'}
print(aset)
bset = {1, 1, 2, 'a', 3}
print(bset)

# dict: An unordered collection of unique key-value pairs; keys must be hashable.
ad = {1: 'one',
      2: 'two'}
bd = {'a': [1, 2, 3],
     'b': 'a string'}

#Testing the type of variables
a = '123'
print(type(a))
# Out: <class 'str'>
b = 123
print(type(b))     

i = 7
if isinstance(i, int):
    i += 10
elif isinstance(i, str):
    i = int(i)
    i += 1
print('i:{0:d}'.format(i))  

# None
x = None
if x is None:
    print('Not a surprise, I just defined x as None.')

# Converting between datatypes
astr = '123'
bint = int(astr)    

astr2 = '123.456'
bfloat = float(astr2)
#cint = int(astr2) # ValueError: invalid literal for int() with base 10: '123.456'
dint = int(bfloat) # 123

hello = 'hello'
list(hello) # ['h', 'e', 'l', 'l', 'o']
set(hello) # {'o', 'e', 'l', 'h'}
tuple(hello) # ('h', 'e', 'l', 'l', 'o')

from enum import Enum
class Color(Enum):
    red = 1
    green = 2
    blue = 3
print(Color.red) # Color.red
print(Color(1)) # Color.red
print(Color['red']) # Color.red
print(Color.red.value) # 1
print([c for c in Color]) # [<Color.red: 1>, <Color.green: 2>, <Color.blue: 3>]
