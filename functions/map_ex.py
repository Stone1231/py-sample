name_lengths = map(len, ["Mary", "Isla", "Sam"])
print(list(name_lengths)) # [4, 4, 3]
print(list(name_lengths)) # [] 再取就空的

a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]
print(list(map(lambda x, y, z : 2.5*x + 2*y - z, a, b, c)))

day, month, year = map(int, '11-09-2012'.split('-'))
print(month) # '09' -> 9