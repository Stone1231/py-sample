from array import array

a1 = array('l')
a2 = array('u', 'hello \u2641')
a3 = array('l', [1, 2, 3, 4, 5])
a4 = array('d', [1.0, 2.0, 3.14])

print(a1)
print(a2)
print(a3)
print(a4)

array1 = array('i', [10,20,30,40,50])
array1.insert(1,60)
for x in array1:
    print(x)

array1.remove(40)
for x in array1:
    print(x)

print(array1.index(30))

array1.reverse()
for x in array1:
    print(x)