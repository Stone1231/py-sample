# from packages.package1 import module1 as module1
from . import module1

def fun():
    module1.fun()
    print('package1 - module2')   

# from .module1 import fun as module1_fun 
# def fun():
#     module1_fun()
#     print('package1 - module2')  