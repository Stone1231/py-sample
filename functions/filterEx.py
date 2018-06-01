names = ['Fred', 'Wilma', 'Barney']

def long_name(name):
    return len(name) > 5

print(list(filter(long_name, names)))

res = [name for name in names if len(name) > 5] 
print(res)

from itertools import filterfalse
res = list(filterfalse(None, [1, 0, 2, [], '', 'a'])) # discards 1, 2, 'a'
print(res)

# Usage with function
res = list(filterfalse(long_name, names))
print(res)