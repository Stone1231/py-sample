def normal(n):
    if n in [0,1]:
        return n

    a = 0
    b = 1
    for i in range(0, n-1):
        temp = b
        b = a + b
        a = temp
    return b 

def bad1(n):
    count = 1
    for i in range(n):
        if i > 1:
            count += bad1(n-i)
    return count   

def bad2(n):
    if n in [0,1]:
        return n
    else: 
        return bad2(n-1) + bad2(n-2)        

count = 36
import time
tStart = time.time() 
print(normal(count))
tEnd = time.time()
print("normal ex: %f sec" % (tEnd - tStart))  

tStart = time.time() 
print(bad1(count))
tEnd = time.time()
print("bad1 ex: %f sec" % (tEnd - tStart))

tStart = time.time() 
print(bad2(count))
tEnd = time.time()
print("bad2 ex: %f sec" % (tEnd - tStart))           