#Using a default value
def describe_pet(name, animal='dog'): 
    """Display information about a pet.""" 
    print("\nI have a " + animal + ".") 
    #print("Its name is " + name + ".") 
    print("Its name is {}.".format(name))

describe_pet(1)
describe_pet(1.1)
describe_pet('harry', 'hamster') 
describe_pet('willie')

#return value
def get_full_name(first, last): 
    """Return a neatly formatted full name.""" 
    full_name = first + ' ' + last 
    return full_name.title() 
musician = get_full_name('jimi', 'hendrix') 
print(musician)

#Collecting an arbitrary number of arguments
def make_pizza(size, *toppings): 
    """Make a pizza.""" 
    print("\nMaking a " + size + " pizza.") 
    print("Toppings:") 
    for topping in toppings: 
        print("- " + topping) 
make_pizza('small', 'pepperoni') 
make_pizza('large', 'bacon bits', 'pineapple') 
make_pizza('medium', 'mushrooms', 'peppers', 'onions', 'extra cheese')

def add(*num):
    return sum(num)
print(add(1,2,3,4))

#Collecting an arbitrary number of keyword arguments
def build_profile(first, last, **user_info): 
    """Build a user's profile dictionary.""" 
    # Build a dict with the required keys. 
    profile = {'first': first, 'last': last} 
    # Add any other keys and values. 
    for key, value in user_info.items(): 
        profile[key] = value 
    return profile 
    # Create two users with different kinds 
    # of information. 
user_0 = build_profile('albert', 'einstein', location='princeton') 
user_1 = build_profile('marie', 'curie', location='paris', field='chemistry') 
user_2 = build_profile('stone', 'rock', location='paris', field='chemistry', bb='xxx')

print(user_0) 
print(user_1) 
print(user_2) 
