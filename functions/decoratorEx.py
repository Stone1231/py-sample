import types

#ex1
def super_secret_function(f):
    print("do something")
    return f

@super_secret_function
def my_function():
    print("This is my secret function.")

my_function()    

#ex2 disabled
def disabled(f):
    """
    This function returns nothing, and hence removes the decorated function
    from the local scope.
    """
    pass

@disabled
def my_function2():
    print("This function can no longer be called...")
try:
    my_function2()
except Exception as identifier:
    print(identifier)  


#ex3 *args, **kwargs
def print_args(func):
    def inner_func(*args, **kwargs):
        print(args)
        print(kwargs)
        return func(*args, **kwargs) #Call the original function with its arguments.
    return inner_func

@print_args
def multiply(num_a, num_b):
    return num_a * num_b    

print(multiply(3, 5))    
print()
print(multiply(num_a=3, num_b=5))    
#print(multiply(num_a=3, 5)) #error! positional argument follows keyword argument
print(multiply(3, num_b=5))  

#ex4 class
class Decorator(object):
    """Simple decorator class."""
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print('Before the function call.')
        res = self.func(*args, **kwargs)
        print('After the function call.')
        return res

@Decorator
def testfunc():
    print('Inside the function.')
testfunc()
# Before the function call.
# Inside the function.
# After the function call.

# Note that a function decorated with a class decorator 
# will no longer be considered a "function" from type-checking perspective:
print(isinstance(testfunc, types.FunctionType))
# False
print(type(testfunc))
# <class '__main__.Decorator'>

#ex5 Decorating Methods
class CountCallsDecorator(object):
    def __init__(self, func):
        self.func = func
        self.ncalls = 0 # Number of calls of this method
    def __call__(self, *args, **kwargs):
        self.ncalls += 1 # Increment the calls counter
        return self.func(*args, **kwargs)
    def __get__(self, instance, cls):
        return self if instance is None else types.MethodType(self, instance)
class Test(object):
    def __init__(self):
        pass
    @CountCallsDecorator
    def do_something(self):
        return 'something was done'
a = Test()
a.do_something()
a.do_something.ncalls # 1
b = Test()
print(b.do_something())
print(b.do_something.ncalls) # 2

#ex6 Decorator with arguments (decorator factory)
def decoratorfactory(message):
    def decorator(func):
        def wrapped_func(*args, **kwargs):
            print('The decorator wants to tell you: {}'.format(message))
            return func(*args, **kwargs)
        return wrapped_func
    return decorator

@decoratorfactory('Hello World')
def test():
    pass
test()

#ex6-2 Decorator classes
def decoratorfactory2(*decorator_args, **decorator_kwargs):
    class Decorator(object):
        def __init__(self, func):
            self.func = func
        def __call__(self, *args, **kwargs):
            print('Inside the decorator with arguments {}'.format(decorator_args))
            return self.func(*args, **kwargs)
    return Decorator

@decoratorfactory2(10)
def test2():
    pass
test2()

#ex7 Using a decorator to time a function
import time
def timer(func):
    def inner(*args, **kwargs):
        t1 = time.time()
        f = func(*args, **kwargs)
        t2 = time.time()
        print('Runtime took {0} seconds'.format(t2-t1))
        return f
    return inner
@timer
def test3():
    pass
test3()

#ex8 Create singleton class with a decorator
def singleton(cls):
    instance = [None]
    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]
    return wrapper

@singleton
class SomeSingletonClass:
    x = 2
    def __init__(self):
        print("Created!")    

instance = SomeSingletonClass() # prints: Created!
instance = SomeSingletonClass() # doesn't print anything
print(instance.x) # 2
instance.x = 3
print(SomeSingletonClass().x) # 3 