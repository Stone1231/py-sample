# Sets (沒有一定的順序) 
# - They are mutable and new elements can be added once sets are defined
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # duplicates will be removed
#> {'orange', 'banana', 'pear', 'apple'}

a = set('abracadabra')
print(a) # unique letters in a 
#> {'a', 'r', 'b', 'c', 'd'}

a.add('z')
print(a)
#> {'a', 'c', 'r', 'b', 'z', 'd'}

# Frozen Sets - They are immutable and new elements cannot added after its defined.
b = frozenset('asdfagsa')
print(b)
#> frozenset({'f', 'g', 'd', 'a', 's'})

cities = frozenset(["Frankfurt", "Basel","Freiburg"])
print(cities)
#> frozenset({'Frankfurt', 'Basel', 'Freiburg'})

# Intersection
ex1 = {1, 2, 3, 4, 5}.intersection({3, 4, 5, 6}) # {3, 4, 5}
ex2 = {1, 2, 3, 4, 5} & {3, 4, 5, 6} # {3, 4, 5}

# Union
ex3 = {1, 2, 3, 4, 5}.union({3, 4, 5, 6}) # {1, 2, 3, 4, 5, 6}
ex4 = {1, 2, 3, 4, 5} | {3, 4, 5, 6} # {1, 2, 3, 4, 5, 6}

# Difference
ex5 = {1, 2, 3, 4}.difference({2, 3, 5}) # {1, 4}
ex6 = {1, 2, 3, 4} - {2, 3, 5} # {1, 4}

# Symmetric difference with
ex7 = {1, 2, 3, 4}.symmetric_difference({2, 3, 5}) # {1, 4, 5}
ex8 = {1, 2, 3, 4} ^ {2, 3, 5} # {1, 4, 5}

# Superset check
ex9 = {1, 2}.issuperset({1, 2, 3}) # False
ex10 = {1, 2} >= {1, 2, 3} # False

# Subset check
ex11 = {1, 2}.issubset({1, 2, 3}) # True
ex12 = {1, 2} <= {1, 2, 3} # True

# Disjoint check
ex13 = {1, 2}.isdisjoint({3, 4}) # True
ex14 = {1, 2}.isdisjoint({1, 4}) # False

# Existence check
2 in {1,2,3} # True
4 in {1,2,3} # False
4 not in {1,2,3} # True

# Add and Remove
s = {1,2,3}
s.add(4) # s == {1,2,3,4}
s.discard(3) # s == {1,2,4}
s.discard(5) # s == {1,2,4}
s.remove(2) # s == {1,4}
s.remove(2) # KeyError!

restaurants = ["McDonald's", "Burger King", "McDonald's", "Chicken Chicken"]
unique_restaurants = set(restaurants)
print(unique_restaurants)
# prints {'Chicken Chicken', "McDonald's", 'Burger King'}

list(unique_restaurants)
# ['Chicken Chicken', "McDonald's", 'Burger King']

#It's also common to see this as one line:
# Removes all duplicates and returns another list
list(set(restaurants))