a_str = 'Hello World'
print(a_str) # Hello World
print(a_str[0]) # H
print(a_str[0:5]) # Hello

first_name = 'albert' 
last_name = 'einstein' 
full_name = first_name + ' ' + last_name 
print(full_name)  

s = """w'o"w"""
print(s)
print(repr(s)) # Output: '\'w\\\'o"w\''
print(str(s)) # Output: 'w\'o"w'

try:
    print(eval(str(s)) == s) # Gives a SyntaxError
except SyntaxError as e:
    print(e)
    pass    

print(eval(repr(s)) == s) # Output: True

from datetime import datetime
now = datetime.now()
print(str(now))
print(repr(now))

