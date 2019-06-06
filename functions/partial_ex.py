from functools import partial

def xy(x, y):
    if y in (3,4,5):
        return x**y
    raise NumberNotInRangeException("You should provide a valid exponent")

raise_to_three = partial(xy, y=3)
raise_to_four = partial(xy, y=4)
raise_to_five = partial(xy, y=5)    
print(raise_to_three(2)) #8 (2 ** 3)
print(raise_to_four(2)) #16 (2 ** 4)
print(raise_to_five(2)) #32 (2 ** 5)