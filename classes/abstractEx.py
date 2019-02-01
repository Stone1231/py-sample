import abc

class Abstract(abc.ABC):

    @abc.abstractmethod
    def aMethod(self):
        raise NotImplementedError("Should have implemented this")

class AClass(Abstract):
    def aMethod(self):
        print("AClass")

class BClass(Abstract):
    def bMethod(self):
        print("BClass")     

objA = AClass()
objA.aMethod()         

#TypeError: Can't instantiate abstract class BClass with abstract methods aMethod
objB = BClass()
objB.bMethod()    