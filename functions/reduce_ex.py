from functools import reduce

total = reduce(lambda a, x: a + x, [0, 1, 2, 3, 4])
print(total) #=>10

fmax = lambda a,b: a if (a > b) else b
fmin = lambda a,b: a if (a < b) else b
print(reduce(fmax, [47,11,42,102,13]))
print(reduce(fmin, [47,11,42,102,13]))

print(reduce(lambda x, y: x*y, range(44,50))/reduce(lambda x, y: x*y, range(1,7)))

orders = [ 
    [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
    [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
    [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
    [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] 
    ]
min_order = 500
invoice_totals = list(map(lambda x: [x[0]] + list(map(lambda y: y[1]*y[2], x[1:])), orders))
print (invoice_totals)
invoice_totals = list(map(lambda x: [x[0]] + [reduce(lambda a,b: a + b, x[1:])], invoice_totals))
print (invoice_totals)
invoice_totals = list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10), invoice_totals))
print (invoice_totals)
